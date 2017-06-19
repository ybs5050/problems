
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Asus
 */
public class Compress {
    
    public static String condense(String str) {
        
        LinkedHashMap<String, Integer> map = new LinkedHashMap<>();
        StringBuilder sb = new StringBuilder("");
        StringBuilder sb2 = new StringBuilder("");
        String lastChar = "";
        for(int i = 0; i < str.length(); i++) {
            if(map.get(Character.toString(str.charAt(i))) == null) {
                map.put(Character.toString(str.charAt(i)), 1);
                lastChar = Character.toString(str.charAt(i));
            } else {
                if (lastChar.charAt(0) == str.charAt(i)) {
                    map.put(lastChar, map.get(lastChar) + 1);
                } else {
                    sb2.append(str.charAt(i));
                    sb2.append(i);
                    map.put(sb2.toString(), 1);
                    lastChar = sb2.toString();
                    sb2 = new StringBuilder("");
                }
            }
        }
        
        for(Map.Entry<String, Integer> entry : map.entrySet()) {
            sb.append(entry.getKey().charAt(0));
            sb.append(entry.getValue());      
        }
        
        return str.length() > sb.length() ? sb.toString() : str;
        
    }
    
    public static String condense2(String str) {
        StringBuilder sb = new StringBuilder();
        char lastChar = str.charAt(0);
        int conc = 1; 
        for(int i = 1; i < str.length(); i++) {
            if(str.charAt(i) == lastChar) {
                // Count consecutive characters
                conc+=1;
                lastChar = str.charAt(i);
            } else {
                // Add previous characters to sb
                sb.append(lastChar);
                sb.append(conc);    
                
                // Reset to current
                conc = 1;
                lastChar = str.charAt(i);
            }
            
        }
        // Add last consecutive characters
        sb.append(lastChar);
        sb.append(conc);    
        return sb.toString();
    }
    
}
