// Desafio Game TicTacToe
#include<iostream>
#include<stdlib.h>
using namespace std;

struct Move{ 
    int row, col; 
}; 
 
// Computador e jogador são definidos globalmente e vamos atribuir "X" a quem for o primeiro a jogar
char computer, player; 

// Array de posição é usado para mapear a posição dada pelo jogador para a célula apropriada do tabuleiro
int position[9][2] = {{0,0},{0,1},{0,2},{1,0},{1,1},{1,2},{2,0},{2,1},{2,2}};


// Esta função é usada para imprimir o tabuleiro sempre que o usuário faz um movimento
void drawBoard(char board[3][3]){
    cout << "----++---++----" << endl;
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            cout << "| ";
            if(board[i][j] == '-'){
                cout << " " << " |";
            }
            else{
                if(board[i][j]=='X') cout << "X |";
                else cout << "O |";
            }
        }
        cout << "\n----++---++----" << endl;
    }
}

