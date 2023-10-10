/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package mypack;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import javax.jws.WebService;
import javax.jws.WebMethod;
import javax.jws.WebParam;

/**
 *
 * @author cs3
 */
@WebService(serviceName = "StockDataService")
public class StockDataService {

    /**
     * Web service operation
     */
    @WebMethod(operationName = "getNSE")
    public int getNSE() {
        int nse=0;
        try{    //Driver specification management system
            Class.forName("org.apache.derby.jdbc.ClientDriver");
            Connection con=DriverManager.getConnection("jdbc:derby://localhost:1527/StockDatadb", "user1", "user1@123");
            Statement stmt=con.createStatement();
            ResultSet rs=stmt.executeQuery("SELECT * FROM STOCKDATA");
            rs.next();
            nse=rs.getInt("NSE");
            con.close();
        }
        catch(Exception e)
        {
       
            
        }
        return nse;
    }

    /**
     * Web service operation
     */
    @WebMethod(operationName = "getBSE")
    public int getBSE() {
         int bse=0;
        try{    //Driver specification management system
            Class.forName("org.apache.derby.jdbc.ClientDriver");
            Connection con=DriverManager.getConnection("jdbc:derby://localhost:1527/StockDatadb", "user1", "user1@123");
            Statement stmt=con.createStatement();
            ResultSet rs=stmt.executeQuery("SELECT * FROM STOCKDATA");
            rs.next();
            bse=rs.getInt("BSE");
            con.close();
        }
        catch(Exception e)
        {
       
            
        }
        //TODO write your implementation code here:
        return bse;
    }

    /**
     * Web service operation
     */
    @WebMethod(operationName = "getGOLDRATE")
    public int getGOLDRATE() {
         int goldrate=0;
        try{    //Driver specification management system
            Class.forName("org.apache.derby.jdbc.ClientDriver");
            Connection con=DriverManager.getConnection("jdbc:derby://localhost:1527/StockDatadb", "user1", "user1@123");
            Statement stmt=con.createStatement();
            ResultSet rs=stmt.executeQuery("SELECT * FROM STOCKDATA");
            rs.next();
            goldrate=rs.getInt("GOLDRATE");
            con.close();
        }
        catch(Exception e)
        {
       
            
        }
        //TODO write your implementation code here:
        return goldrate;
    }
}
