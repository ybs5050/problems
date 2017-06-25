/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Asus
 */
public class TransposeNinety {
    
     // My approach
    public static void printMatrix(int n) {
        int[][] arr = new int[n][n];
        int[][] arr2 = new int[n][n];
        int count = 1;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                arr[i][j] =count;
                count++;
            }
        }
        // Print original
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
        
        // 90 degree transpose
        /*
        arr2[0][0] = arr[0][2]
        arr2[0][1] = arr[1][2]
        arr2[0][2] = arr[2][2]
        */
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                arr2[i][j] = arr[n-j-1][i];
            }
        }
        
        // print transposed
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                System.out.print(arr2[i][j] + " ");
            }
            System.out.println();
        }
        
	
    }
    
    // Book approach
    /*
    for i = to n
        temp = top[i];
        top[i] = left[i]
        left[i] = bottom[i]
        bottom[i] = right[i]
        right[i] = temp
    */
    public static void rotate(int n) {
        
        int[][] matrix = new int[n][n];
        int count = 1;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                matrix[i][j] =count;
                count++;
            }
        }
        
        for(int i = 0; i < n/2; i++) {
            
            for(int j = i; j < n-1-i; j++) {
                int offset = j-i;
                
                // save top
                int top = matrix[i][j];
                
                /// left to top
                matrix[i][j] = matrix[n-1-i-offset][i];
                
                // bottom to left
                matrix[n-1-i-offset][i] = matrix[n-1-i][n-1-i-offset];
                
                // right to bottom
                matrix[n-1-i][n-1-i-offset] = matrix[j][n-1-i];
                
                // top to right
                matrix[j][n-1-i] = top;
            }
        }
        
         // print transposed
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }
    
}
