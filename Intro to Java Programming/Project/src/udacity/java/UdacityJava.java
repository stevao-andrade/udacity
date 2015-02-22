/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package udacity.java;

/**
 *
 * @author Stevao
 */
public class UdacityJava {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
                java.util.Properties props = System.getProperties();
        System.out.println("OS: " + props.get("os.name") 
            + " " + props.get("os.version"));
        System.out.println("Java: " + props.get("java.vendor") 
            + " " + props.get("java.version"));
        String classpath = "" + props.get("java.class.path");
        String ide;
        if (classpath.contains("bluej"))
            ide = "BlueJ";
        else if (props.get("com.horstmann.codecheck") != null)
            ide = "Udacity";
        else 
            ide = "Unknown";
        System.out.println("IDE: " + ide);
        System.out.println("Secret code: " +
            Math.abs(ide.hashCode() % 10000));
    }
}
