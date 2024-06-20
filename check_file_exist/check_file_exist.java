import java.nio.file.Files;
import java.nio.file.Paths;

/* 
 * todo verify
 * 先导入了java.nio.file.Files和java.nio.file.Paths两个类。Paths.get(filePath)方法用于获取filePath路径的Path对象。
 * 接着，Files.exists(Path)方法用以检查通过Paths.get()方法得到的文件路径是否存在。如果文件存在，它将返回true，否则返回false。
 * run cmd：
 * javac check_file_exist.java
 * java check_file_exist
 */

public class FileExistenceCheck {
    public static void main(String[] args) {
        String filePath = "./a.txt";

        // 使用Paths获取文件路径，Files.exists()检查文件是否存在
        if (Files.exists(Paths.get(filePath))) {
            System.out.println(filePath + " exists.");
        } else {
            System.out.println(filePath + " does not exist.");
        }
    }
}