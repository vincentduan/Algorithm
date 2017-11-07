import entity.SLNode;
import service.SLNodeService;

/**
 * Created with IntelliJ IDEA.
 * User: vincent
 * Date: 2017/11/6
 * Time: 15:31
 */
public class Test {
    public static void main(String[] args) {
        SLNodeService slNodeService = new SLNodeService();
        SLNode newSLNode = slNodeService.createNewSLNode();
        newSLNode.setData("a");
        SLNode newSLNode2 = slNodeService.createNewSLNode();
        newSLNode2.setData("b");
        newSLNode.setNext(newSLNode2);
        SLNode newSLNode3 = slNodeService.createNewSLNode();
        newSLNode2.setData("c");
        newSLNode2.setNext(newSLNode3);
    }
}
