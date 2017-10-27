# rpc
Simples RPC trabalho

# Rodar execução

> Baixar o projeto de socket communication `git@github.com:kauehmoreno/socket-communication.git`
> executar `make VENV - make setup - make run `


# No projeto RPC

executar apenas - `make run `

```
 Após a execução um arquivo storage.dat será criado no lado servidor - projeto de socket- communication...

 com todas as etapas catalogados simulando um log de operação


 msgpack é usado como protocolo de comunicao entre o canal - esse protocolo
 transforma em binário e trafega pela camada de transporte sendo convertido na outra
 ponta, funciona como um pickle , porém melhor.

```
### Idéia
> Simular um RPC que executa jobs um servidor - estes jobs executaria os testes e mandaria
> sms e email ao terminar com todo o processo descrito nos jobs..
> Além de passar o fallback ao cliente que solicitou para que ele possa fazer algum coisa
