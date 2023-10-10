/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package mypack;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import javax.jws.WebService;
import javax.jws.WebMethod;
import javax.jws.WebParam;

/**
 *
 * @author sies
 */
@WebService(serviceName = "NaacWebsite")
public class NaacWebsite {

    /**
     * Web service operation
     */
    @WebMethod(operationName = "getRatings")
    public String getRatings(@WebParam(name = "collegenames") String collegenames) {
        String cname="";
        try{
        Class.forName("org.apache.derby.jdbc.ClientDriver");
        Connection con=DriverManager.getConnection("jdbc:derby://localhost:1527/USER1","user1","user1@123");
        Statement stmt=con.createStatement();
        /*PreparedStatement pstmt=con.prepareStatement("SELECT * FROM NAACDATA WHERE COLLEGENAME=?");
        pstmt.setString(1,collegenames);*/
        
        ResultSet rs=stmt.executeQuery("SELECT * FROM NAACDATA WHERE COLLEGENAME='" +collegenames+"'");
        rs.next();
        cname=rs.getString("RATINGS");
    }
        catch(Exception e)
        {
            e.printStackTrace();
        }
    return cname;
    }
}