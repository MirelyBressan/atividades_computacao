
#include <stdio.h>
#include <stdlib.h>

//lista encadeada para fila de clientes
typedef struct No {
    int numero;          
    char prioridade;     
    struct No *prox;     
} No;

No *head = NULL;

int contComum = 1;
int contPrioridade = 301;

//criando um novo nó
No* criarNo(char prioridade) {
    No* novo = (No*)malloc(sizeof(No));
    novo->prioridade = prioridade;

    if (prioridade == 'C')
        novo->numero = contComum++;
    else
        novo->numero = contPrioridade++;

    novo->prox = NULL;
    return novo;
}

//inserir clientes sem prioridades
void inserirSemPrioridade(No* novo) {
    if (head == NULL) {
        head = novo;
    } else {
        No *temp = head;
        while (temp->prox != NULL)
            temp = temp->prox;
        temp->prox = novo;
    }
}

// inserir clientes com prioridade
void inserirComPrioridade(No* novo) {
    
    if (head == NULL) {
        head = novo;
        return;
    }

    if (head->prioridade == 'C') {
        novo->prox = head;
        head = novo;
        return;
    }

    No *temp = head;
    while (temp->prox != NULL && temp->prox->prioridade == 'P')
        temp = temp->prox;

    novo->prox = temp->prox;
    temp->prox = novo;
}

//função de inserir cliente na fila
void inserir() {
    char tipo;
    printf("\nDigite o tipo de senha: P -> PRIORITÁRIO ou C -> COMUM): ");
    scanf(" %c", &tipo);

    No* novo = criarNo(tipo);

    if (head == NULL)
        head = novo;
    else if (tipo == 'C')
        inserirSemPrioridade(novo);
    else
        inserirComPrioridade(novo);

    printf("Senha %c%d criada com sucesso!\n", tipo, novo->numero);
}

//imprimir todos os clientes na fila
void imprimirFilaClientes() {
    if (head == NULL) {
        printf("\nA fila está vazia!\n");
        return;
    }

    No* temp = head;
    printf("\n--- FILA DE CLIENTES ---\n");
    while (temp != NULL) {
        printf("Senha %c%d\n", temp->prioridade, temp->numero);
        temp = temp->prox;
    }
}

//remover cliente da fila
void atenderCliente() {
    if (head == NULL) {
        printf("\nNão há nenhum cliente na fila.\n");
        return;
    }

    No* temp = head;
    printf("\nPróximo cliente: Senha %c%d\n", temp->prioridade, temp->numero);
    head = head->prox;
    free(temp);
}

//imprimir o menu principal
void menu() {
    int opcao;
    do {
        printf("\n--------------> MENU <--------------\n");
        printf("Adicionar o cliente à fila - Digite 1\n");
        printf("Mostrar a fila de clientes - Digite 2\n");
        printf("Chamar o próximo cliente - Digite 3\n");
        printf("Sair - Digite 4\n");
        printf("Digite uma das opções acima: ");
        scanf("%d", &opcao);

        switch(opcao) {
            case 1: inserir(); break;
            case 2: imprimirFilaClientes(); break;
            case 3: atenderCliente(); break;
            case 4: printf("\nFinalizando o programa...\n"); break;
            default: printf("\nOpção não permitida! Tente novamente.\n");
        }
    } while (opcao != 4);
}

int main() {
    menu();
    return 0;
}
