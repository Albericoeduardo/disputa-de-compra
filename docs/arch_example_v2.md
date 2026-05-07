# Arquitetura v2 - DDD (Estado Atual Implementado)

## 1. Mapa de Pastas (Real no Projeto)

```text
chargeback/
├── domain/                                # Nucleo de negocio (DDD)
│   ├── entities/
│   │   ├── contestacao.py                 # Aggregate Root do fluxo principal
│   │   └── cliente.py
│   ├── value_objects/
│   │   ├── status_contestacao.py
│   │   ├── tipo_contestacao.py
│   │   └── tipo_anexo.py
│   ├── repositories/                      # Interfaces (contratos)
│   │   ├── icontestacao_repo.py
│   │   ├── icliente_repo.py
│   │   └── iprazo_repo.py
│   └── services/
│       └── contestacao_service.py         # Regras de negocio (transicao, deadline, unicidade)
│
├── aplication/                            # Camada de aplicacao (nome atual do projeto)
│   ├── casos_de_uso/
│   │   ├── abrir_contestacao_caso_de_uso.py
│   │   ├── atualizar_status_contestacao_caso_de_uso.py
│   │   ├── anexar_documento_caso_de_uso.py
│   │   ├── buscar_contestacao_caso_de_uso.py
│   │   └── listar_contestacoes_caso_de_uso.py
│   └── serializers/
│       ├── contestacao_serializer.py
│       ├── cliente_serializer.py
│       └── anexo_serializer.py
│
├── infra/                                 # Infraestrutura tecnica
│   ├── models/
│   │   ├── contestacao_model.py
│   │   ├── cliente_model.py
│   │   ├── historico_contestacao_model.py
│   │   ├── anexo_contestacao_model.py
│   │   └── prazo_etapa_model.py
│   └── repositorios/
│       ├── contestacoes_repo_impl.py
│       ├── clientes_repo_impl.py
│       └── prazo_repo_impl.py
│
├── views/                                 # Adaptadores HTTP (DRF)
│   ├── contestacao_view.py
│   └── anexar_documentos.py
│
├── urls.py                                # Rotas HTTP
├── settings.py                            # Config Django/DRF
├── apps.py                                # AppConfig
└── models.py                              # Exposicao dos models Django da app
```

## 2. Responsabilidades por Camada

### Domain
- Define regras invariantes do negocio.
- Nao conhece Django, DRF ou banco.
- Contem contratos de repositorio e servicos de dominio.

### Application (aplication)
- Orquestra casos de uso.
- Recebe dados validados, chama dominio e persiste via interfaces.
- Nao faz regra tecnica de framework, apenas fluxo de negocio.

### Infrastructure (infra)
- Implementa persistencia real com Django ORM.
- Mapeia entidade <-> modelo.
- Registra historico, anexos e consulta de prazos.

### Interface de Entrada (views/urls/serializers)
- Converte HTTP em dados de aplicacao.
- Retorna respostas padronizadas de sucesso/erro.

## 3. Fluxo Atual de Requisicao (Geral)

```text
Request HTTP
  -> View DRF
    -> Serializer (validacao de entrada)
      -> Caso de Uso (application)
        -> Service de Dominio (regras)
          -> Repositorio (interface de dominio)
            -> Repo Impl Django (infra)
              -> Model ORM
                -> Banco SQLite
      <- Resultado de negocio
    <- Response padronizada
<- HTTP Response
```

## 4. Fluxos Principais Implementados

### 4.1 Abrir Contestacao

```text
POST /contestacoes/
  -> ContestacaoCollectionView.post
    -> ContestacaoViewSerializer
      -> AbrirContestacaoCasoDeUso
        -> ContestacaoService.pode_abrir_contestacao
        -> ClienteRepo.obter_ou_criar
        -> ContestacaoService.calcular_data_limite
        -> ContestacaoRepo.salvar
        -> ContestacaoRepo.registrar_historico
  <- 201 (success=true, data=contestacao)
```

Regras aplicadas:
- Unicidade por (token_transacao, tipo) para registros ativos.
- Status inicial ABERTO.
- Deadline inicial por etapa/bandeira.
- Registro de historico na abertura.

### 4.2 Atualizar Etapa/Status

```text
PATCH /contestacoes/{id}/
  -> ContestacaoDetailView.patch
    -> AtualizarStatusContestacaoSerializer
      -> AtualizarStatusContestacaoCasoDeUso
        -> ContestacaoRepo.buscar_por_id
        -> ContestacaoService.pode_transicionar_status
        -> ContestacaoService.calcular_data_limite
        -> ContestacaoRepo.atualizar
        -> ContestacaoRepo.registrar_historico
  <- 200 ou erro de conflito/not found
```

Regras aplicadas:
- Matriz de transicoes validas de status.
- Bloqueio de transicao quando prazo da etapa expirou.
- Reabertura fora do escopo do fluxo principal atual.

### 4.3 Anexar Evidencia

```text
POST /contestacoes/{id}/anexos/
  -> AnexarDocumentosView.post
    -> AnexoContestacaoSerializer
      -> AnexarDocumentoCasoDeUso
        -> ContestacaoRepo.buscar_por_id
        -> valida status nao encerrado
        -> ContestacaoRepo.anexar_documento
  <- 201 ou erro de dominio
```

Regras aplicadas:
- Nao permite anexar evidencia em contestacao encerrada.

### 4.4 Consultas

```text
GET /contestacoes/                     # lista com filtros
GET /contestacoes/{id}/                # detalhe
GET /contestacoes/{id}/anexos/         # evidencias por contestacao
```

## 5. Endpoints Atuais

- `POST /contestacoes/`
- `GET /contestacoes/`
- `GET /contestacoes/{contestacao_id}/`
- `PATCH /contestacoes/{contestacao_id}/`
- `POST /contestacoes/{contestacao_id}/anexos/`
- `GET /contestacoes/{contestacao_id}/anexos/`

## 6. Observacao Arquitetural

No guia conceitual original, a camada se chama `application`; no projeto atual a pasta esta como `aplication`. A estrutura funcional segue DDD e pode ser renomeada futuramente para padronizacao sem alterar o desenho arquitetural.
