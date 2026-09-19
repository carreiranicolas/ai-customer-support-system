# Anotações 

## O que é um AI Agent?

Um AI Agente pode ser confundida com um LLM padrão como chat GPT, por exemplo, mas não é essa a ideia. No chat GPT, você pergunta e ele responde.

Um AI Agente utiliza sim um LLM para pensar, como cérebro, mas um Agent irá além, ele irá agir até que o trabalho atribuído seja concluído. Ele observa, Age, Pensa, Repete, tudo isso em um ciclo para concluir a tarefa

Pense como se fosse literalmente um humano no lugar. Ao atribuir uma tarefa, ele irá olhar pra ver como ele poder fazer, tomar decisões, agir, pensar..

Dessa forma, podemos definir um agente como um sistema que pode perceber o ambiente, tomar decisões, tomar ações e trabalhar entorno de um objetivo de forma autonoma



## O que é Agentic AI?

O agentic AI é basicamente um ecossistema de AI Agents. Como vimos anteriormente, um AI Agent irá pensar e agir de forma autonoma. Quando temos um sistema, podemos ter mais de um AI Agent especializado para determinado fim. Exemplo: 

- Support Agent: Faria o contato e a tratativa inicial
- Manager Agent: Teria privilégios maiores e seria responsável por analisar e tomar decisões
- Risk Agent: Validaria se há risco antes de uma tomada de decisão

Portanto, você teria um ecossistema de agentes que observam, pensam, agem de maneira autonôma e trabalhando em funções especificas, assim como em uma corporação mesmo


## O que é uma Tool?

Uma Tool é basicamente uma função que será utilizada pelo agente para realizar  determinada ação. Exemplo:

```python
def get_order_details(order_id):
order = Order.objects.get(id=order_id)
return {
"status": order.status,
"carrier": order.carrier,
"tracking": order.tracking_number,
}
```

Se nós temos um cliente por exemplo pedindo extorno de uma compra e nós temos diversas tools (funções) qual o agente irá chamar para utilizar como forma de resposta a esse cliente? Isso é feito a partir da descrição da tool, que descreverá ela de forma detalhada, para que o agente possa refletir e decidir se aquela tool será necessária para a resolução daquele problema em especifico. Isso tudo é feito por meio de um JSON, veja:

```json
{
    "name": "get_order_details",
    "description": "Fetch order details including
    status, carrier, and tracking number.",
    "input_schema": {
        "type": "object",
        "properties": {
            "order_id": {
                "type": "integer",
                "description": "The order ID to look up"
            }
        },
        "required": ["order_id"]
    }
}
```

Acima, nosso agent irá olhar a descrição e até teremos alguns detalhes reçacionados a schema que o auxiliarão no processo

## Agent Loop

O agent loop consiste basicamente no fluxo do agente de: 

Pensar -> Tool -> Checkar

Nesse processo, ao pensar, o agent se pergunta "tenho todas as informações necessárias" e se tiver, ai ele vai pra resposta final, mas se não tiver, ele vai fazer esse processo de uso de tool e check recursivamente. 

Portanto, podemos definir como literalmente o fluxo que é feito até o a realização da tarefa atribuída

## AI Agent Framework

Assim como linguagens de programação que tem frameworks, o campo de AI Agent também tem, sendo alguns deles: LangChain, AutoGen, CrewAI.

Essas bibliotecas python servem para a criação rápida de AI Agents, pois fornecem componentes prontos para usarmos e também integrações com Tools (conexões com serviçõs exernos, DB e APIs)

- LangChain: É o mais famoso, que para além da criação de Agentes, nos permite usar uma "Chain" para decidir em qual sequencia as coisas deverão ser feitas pelo agente

- Autogen: É o framework de colaboração multi-agente, então nele nós definimos agentes atribuindo nome, cargo e um system prompt (você é um support n1..) e a partir disso definimos tarefas e como os agentes podem colaborar uns com os outros

- CrewAI: É similar ao AutoGen. Com ele criamos times de agentes, podendo atribuir nomes, cargos.. Para que cada um deles colaborem juntos para um resultado final


Todos esses frameworks são "automáticos", então a ideia é que aprendamos a forma manual antes.
