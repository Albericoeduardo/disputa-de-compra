# 📘 Contexto do Domínio — Plataforma de Disputa Financeira (Chargeback)

## 🎯 Visão Geral

Sistema para gestão de disputas financeiras (chargebacks) para lojistas.

O sistema acompanha o ciclo completo da disputa entre cliente, lojista e operadora do cartão.

---

## 🧠 Problema de Negócio

Uma disputa ocorre quando um cliente contesta uma transação.

Esse processo envolve:

* Regras da bandeira
* Prazos por etapa
* Envio de evidências
* Decisão final

---

## 🔄 Fluxo da Disputa

1. Transação ocorre
2. Cliente contesta
3. DisputeCase é criado
4. Disputa passa por etapas
5. Evidências são enviadas
6. Decisão final é tomada

---

## 🧩 Conceitos do Domínio

### DisputeCase

* Representa a disputa
* Controla estado e regras
* Garante unicidade por tipo

Regra:

* Não pode existir duas disputas do mesmo tipo na mesma transação

---

### DisputeStage

Etapas:

* OPEN
* UNDER_ANALYSIS
* IN_DISPUTE
* REOPENED
* WON
* LOST

---

### Regras de Reabertura

* Nem toda disputa pode ser reaberta
* Depende do motivo do encerramento

---

### Evidence

* Pode ser enviada múltiplas vezes
* Depende da etapa da disputa
* Pode expirar

---

### Deadline

* Definido por etapa
* Depende da bandeira

---

### Transaction

* Pode gerar múltiplas disputas
* Restrição por tipo

---

### Merchant

* Recebe penalidades acumuladas

---

### Customer

* Origina a disputa

---

### PaymentInfo

* NÃO armazenar dados sensíveis
* Apenas bandeira do cartão

---

## ⚙️ Regras de Negócio

* Múltiplas disputas por transação (tipos diferentes)
* Uma disputa por tipo
* Prazos por etapa
* Evidências múltiplas
* Penalidades acumuladas por lojista

---

## 🚀 Objetivo Técnico

* Python
* Django (infraestrutura)
* Domínio independente

O Django será usado apenas para:

* Persistência
* APIs
* Integrações

---

## 📣 Observação

O modelo evoluirá continuamente.
