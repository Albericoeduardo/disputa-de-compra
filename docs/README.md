# 📘 README — Contexto do Projeto

## 🎯 Objetivo

Este arquivo orienta o agente de IA sobre como navegar pelo contexto do projeto.

---

## 🧠 Visão Geral

Plataforma de gestão de disputas financeiras (chargebacks).

Stack:

* Python
* Django (infraestrutura)
* Domain-Driven Design (DDD)

---

## 📂 Arquivos de Contexto

### `diretrizes.md`

Define como o agente deve agir.

### `contexto-dominio.md`

Define o domínio do problema.

---

## 🧭 Ordem de Leitura

1. diretrizes.md
2. contexto-dominio.md

---

## 🧱 Arquitetura

* `domain/` → domínio (Python puro)
* `application/` → casos de uso
* `infrastructure/` → Django

---

## ⚠️ Regras

* Não ignorar o domínio
* Não gerar CRUD simples
* Não misturar domínio com Django

---

## 🚀 Estado Atual

* Projeto iniciado
* Domínio definido
* Próximo passo: implementação do domínio

---

## 📣 Regra Final

> O domínio vem antes do framework.
