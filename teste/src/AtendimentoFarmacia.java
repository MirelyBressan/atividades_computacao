import java.util.Scanner;

public class AtendimentoFarmacia {
    public static void main(String[] args) {
        Scanner leitura = new Scanner(System.in);

        System.out.print("Digite a quantidade de setores: ");
        int qtSetores = leitura.nextInt();
        leitura.nextLine(); 

        String[] setores = new String[qtSetores];
        int[] clientes = new int[qtSetores];
        int totalClientes = 0;

        for (int i = 0; i < qtSetores; i++) {
            System.out.print("Digite o nome do setor " + (i + 1) + ": ");
            setores[i] = leitura.nextLine();

            System.out.print("Digite a quantidade de clientes no setor " + setores[i] + ": ");
            clientes[i] = leitura.nextInt();
            leitura.nextLine(); 
            totalClientes += clientes[i];
        }

        int tempoTotal = 300;
        int tempoMin = 30;
        int tempoMax = 120;

        System.out.println("\n--- Tempo ideal de atendimento por setor ---");
        for (int i = 0; i < qtSetores; i++) {
            double proporcao = (double) clientes[i] / totalClientes;
            int tempo = (int) Math.round(proporcao * tempoTotal);

            if (tempo < tempoMin) {
                tempo = tempoMin;
            } else if (tempo > tempoMax) {
                tempo = tempoMax;
            }

            System.out.println(setores[i] + ": " + tempo + " segundos");
        }

        leitura.close();
    }
}