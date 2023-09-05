import java.util.Arrays;

public class MultimetroQuebrado {
    public static void main(String[] args) {
        double[] leituras = { 4.5, 4.7, 4.6, 4.8, 4.9, 4.4, 4.5, 4.6, 4.7, 4.8 };
        
        // Imprimir todas as leituras
        System.out.println("Leituras:");
        for (double leitura : leituras) {
            System.out.println(leitura);
        }
        
        // Calcular a média das leituras
        double media = calcularMedia(leituras);
        System.out.println("Média: " + media);
        
        // Calcular o desvio padrão das leituras
        double desvioPadrao = calcularDesvioPadrao(leituras);
        System.out.println("Desvio Padrão: " + desvioPadrao);
        
        // Verificar se o multímetro está operacional
        if (desvioPadrao > media * 0.1) {
            System.out.println("O multímetro está com problemas e não pode ser utilizado.");
        } else {
            System.out.println("O multímetro está operacional.");
        }
    }
    
    public static double calcularMedia(double[] leituras) {
        double soma = 0;
        for (double leitura : leituras) {
            soma += leitura;
        }
        return soma / leituras.length;
    }
    
    public static double calcularDesvioPadrao(double[] leituras) {
        double media = calcularMedia(leituras);
        double somaDiferencasQuadrado = 0;
        for (double leitura : leituras) {
            somaDiferencasQuadrado += Math.pow(leitura - media, 2);
        }
        double variancia = somaDiferencasQuadrado / leituras.length;
        return Math.sqrt(variancia);
    }
}
