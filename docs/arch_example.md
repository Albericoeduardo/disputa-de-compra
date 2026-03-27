── domain/                  # Coração do negócio
│   ├── aggregates/             # Raízes de Aggregates e Entidades internas
│   │   ├── dispute.py          # DisputeCase (Root), Evidence, Stage
│   │   ├── merchant.py         # Merchant (Root) e lógica de penalidades
│   │   └── transaction.py      # Transaction (Root) e PaymentInfo (VO)
│   ├── value_objects.py        # Objetos imutáveis
│   ├── exceptions.py           # Exceções de negócio
│   └── repositories/           # Interfaces
│       ├── dispute_repo.py     # Define COMO buscar/salvar, mas não ONDE
│       └── merchant_repo.py
│
├── application/              # Orquestração
│   ├── use_cases/              # Regras de fluxo
│   │   ├── open_dispute.py     # Fluxo: Validar -> Criar -> Salvar -> Notificar
│   │   └── submit_evidence.py
│   └── dtos.py                 # Objetos de transferência
│
├── infrastructure/           # Detalhes técnicos
│   ├── persistence/            # Persistência de dados
│   │   ├── models.py           # Modelos do Django ORM
│   │   ├── repositories.py     # Implementação real dos Repositories
│   │   └── migrations/         # Migrações do banco
│   ├── api/                    # Interface de Entrada
│   │   ├── views.py            # Controllers do Django / DRF
│   │   ├── serializers.py      # Conversão JSON <-> DTO
│   │   └── urls.py             # Rotas da API
│   └── services/               # Integrações externas

Request HTTP
↓
View
↓
DTO
↓
Use Case
↓
Aggregate
↓
Repository
↓
Repository Django
↓
Banco