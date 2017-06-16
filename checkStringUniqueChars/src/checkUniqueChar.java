
import java.util.HashMap;
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
public class checkUniqueChar {
    
    public static void main(String[] args) {
        boolean test = checkUnique("abcdefg");
        System.out.println(test);
    }
    
    public static boolean checkUnique(String str) {
        
        if(str.length() == 0) {
            return false;
        }
        
        HashMap<Character, Integer> map = new HashMap<>();
        for(int i = 0; i < str.length(); i++) {
            if(map.get(str.charAt(i)) == null) {
                map.put(str.charAt(i), 1);
            } else {
                return false;
            }
        }
        
        //if passed
        
        for(Map.Entry<Character, Integer> entry: map.entrySet()) {
            System.out.println(entry.getKey() + "  " + entry.getValue());
        }
        
        
        return true;
    }
    
}
