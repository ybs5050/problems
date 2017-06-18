/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Asus
 */
public class replaceSpace {
    
    // My appraoch
    public static String replaceSpace(String str) {
        
        StringBuilder finalString = new StringBuilder("");
        String replacement = "%20";
        String[] lists = str.split(" ");
        
        for(int i = 0; i < lists.length; i++) {
            if(lists[i] == " ") {
                finalString.append(replacement);
            } else {
                finalString.append(lists[i]);
            }
        }
        
        return finalString.toString();
        
    }
    
    // Book approach
    
    public void replaceSpaces(char[] str, int length) {
        
        int spaceCount = 0;
        int newLength; 
        
        for(int i = 0; i < str.length; i++) {
            if(str[i] == ' ') {
                spaceCount++;
                
            }
        }
        
        newLength = length + spaceCount * 2;
        for(int i = length-1; i >=0; i++) {
            if(str[i] == ' ') {
                str[newLength - 1] = '0';
                str[newLength - 2] = '2';
                str[newLength - 3] = '%';
                newLength = newLength-3;
            } else {
                str[newLength-1] = str[i];
                newLength = newLength-1;
            }
        }
    }
    
}

