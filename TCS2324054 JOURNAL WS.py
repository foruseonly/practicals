#!/usr/bin/env python
# coding: utf-8

# In[ ]:


PRACTICAL 1
Create a TimeServer webservice in Java and Consume it in java and other technologies like php and .NET

CLIENT

CODE
TimeServerOne.java
*()
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package mypack;

import java.util.Date;
import javax.jws.WebService;
import javax.jws.WebMethod;
import javax.jws.WebParam;

**()
 *
 * @author patol
 */
@WebService(serviceName = "TimeServerOne")
public class TimeServerOne {

    /**
     * Web service operation
     */
    @WebMethod(operationName = "operation1")
    public String operation1() {
        //TODO write your implementation code here:
        return new Date().toString();
    }

    /**
     * Web service operation
     */
    @WebMethod(operationName = "operation2")
    public long operation2() {
        //TODO write your implementation code here:
        return new Date().getTime();
    }
}
OUTPUT
SERVER SIDE
 
CLIENT SIDE
 


PRACTICAL 2
Create a Java WS for performing basic calculations like addition, subtraction ,multiplication and Division and create a java client that consumes the same.

CLIENT
Index.html
CODE
<html>	
	<head>
		<title>CALCULATOR</title>
	</head>
	<body>
		<h3>CALCULATOR</h3>
		<form action="calculate" method="get">
		<table><tr>
			<td><input name="opr1" type="text"/>
			</td>
			<td><select name="Operation">
				<option value="+">+</option>
				<option value="-">-</option>
				<option value="*">*</option>
				<option value="/">/</option>
				<option value="%">%</option>
			    </select>
			</td>
			<td><input name="opr2" type="text"/>
			</td>
			<td><input name="result" type="submit"/>
			</td>
		       </tr>
		</table>
		</form>
	</body></html>

Index.php
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <%
            float first=Float.parseFloat(request.getParameter("h1"));
            float second=Float.parseFloat(request.getParameter("h2"));
            String choice=request.getParameter("operation");
            if (choice.equals("add"))
                    {
    
    try {
	calc.Calculator90_Service service = new calc.Calculator90_Service();
	calc.Calculator90 port = service.getCalculator90Port();
	float result = port.addition(first, second);
	out.println("Result = "+result);
    } catch (Exception ex) {
	// TODO handle custom exceptions here
    }
                    }
            else if(choice.equals("sub")){
                try {
	calc.Calculator90_Service service = new calc.Calculator90_Service();
	calc.Calculator90 port = service.getCalculator90Port();
	float result = port.subtraction(first, second);
	out.println("Result = "+result);
    } catch (Exception ex) {
	// TODO handle custom exceptions here
    }
            }
            else if(choice.equals("multiply")){
                try {
	calc.Calculator90_Service service = new calc.Calculator90_Service();
	calc.Calculator90 port = service.getCalculator90Port();
	float result = port.multiply(first, second);
	out.println("Result = "+result);
    } catch (Exception ex) {
	// TODO handle custom exceptions here
    }
            }
             else if(choice.equals("division")){
                try {
	calc.Calculator90_Service service = new calc.Calculator90_Service();
	calc.Calculator90 port = service.getCalculator90Port();
	float result = port.division(first, second);
	out.println("Result = "+result);
    } catch (Exception ex) {
                
    %>
    
        </form>
        <h1></h1>
    </body>
</html>
OUTPUT
 
PRACTICAL 3
Create a web service that gives – (i) NSE Index, (ii) BSE Index, (iii)Gold Rate. The values are stored in database. Also create a web client for a share trading firm that displays these values on its home page

CODE
STOCKDATADB TABLE
 
STOCKDATASERVICE.JAVA
*()
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

**()
 *
 * @author patol
 */
@WebService(serviceName = "StockDataService")
public class StockDataService {

    /**
     * Web service operation
     */
    @WebMethod(operationName = "getNSE")
    public int getNSE() {
       int nse=0;
        try{
            //driver specification
            Class.forName("org.apache.derby.jdbc.ClientDriver");
            //connecting to database
            Connection con=DriverManager.getConnection("jdbc:derby://localhost:1527/StockDatadb","user1","user1@123");
            //creating java statement object
            Statement stmt=con.createStatement();
            //executing the query and generating resultset
            ResultSet rs=stmt.executeQuery("SELECT * FROM STOCKDATA");
            //bring resultset pointer to the first record
            rs.next();
            //retrieving values from the rs object at a specific column
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
        try{
            //driver specification
            Class.forName("org.apache.derby.jdbc.ClientDriver");
            //connecting to database
            Connection con=DriverManager.getConnection("jdbc:derby://localhost:1527/StockDatadb","user1","user1@123");
            //creating java statement object
            Statement stmt=con.createStatement();
            //executing the query and generating resultset
            ResultSet rs=stmt.executeQuery("SELECT * FROM STOCKDATA");
            //bring resultset pointer to the first record
            rs.next();
            //retrieving values from the rs object at a specific column
            bse=rs.getInt("BSE");
            con.close();
                }
        catch(Exception e)
        {
                }
        return bse;
    }

    /**
     * Web service operation
     */
    @WebMethod(operationName = "getGOLDRATE")
    public int getGOLDRATE() {
         int goldrate=0;
        try{
            //driver specification
            Class.forName("org.apache.derby.jdbc.ClientDriver");
            //connecting to database
            Connection con=DriverManager.getConnection("jdbc:derby://localhost:1527/StockDatadb","user1","user1@123");
            //creating java statement object
            Statement stmt=con.createStatement();
            //executing the query and generating resultset
            ResultSet rs=stmt.executeQuery("SELECT * FROM STOCKDATA");
            //bring resultset pointer to the first record
            rs.next();
            //retrieving values from the rs object at a specific column
            goldrate=rs.getInt("GOLDRATE");
            con.close();
                }
        catch(Exception e)
        {
                }
        return goldrate;
    }
    }
NEWJSP.JSP
<%-- 
    Document   : newjsp
    Created on : 29 Aug, 2023, 6:29:44 PM
    Author     : patol
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <%
        String stock=request.getParameter("stock");
        if(stock.equals ("NSE Index")){
        
        
        
    try {
	mypack.StockDataService_Service service = new mypack.StockDataService_Service();
	mypack.StockDataService port = service.getStockDataServicePort();
	// TODO process result here
	int result = port.getNSE();
	out.println("Result = "+result);
    } catch (Exception ex) {
	// TODO handle custom exceptions here
    }
        }
        else if(stock.equals("BSE Index")){
            
    
    try {
	mypack.StockDataService_Service service = new mypack.StockDataService_Service();
	mypack.StockDataService port = service.getStockDataServicePort();
	// TODO process result here
	int result = port.getBSE();
	out.println("Result = "+result);
    } catch (Exception ex) {
	// TODO handle custom exceptions here
    }
        }
        else
        {
            
                
    
    try {
	mypack.StockDataService_Service service = new mypack.StockDataService_Service();
	mypack.StockDataService port = service.getStockDataServicePort();
	// TODO process result here
	int result = port.getGOLDRATE();
	out.println("Result = "+result);
    } catch (Exception ex) {
	// TODO handle custom exceptions here
    }
    
   

        }
    get_ipython().run_line_magic('>', '')
 

    </body>
</html>
INDEX.JSP
<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <title>TODO supply a title</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
           <form action="newjsp.jsp">
            Enter Your Choice:
            <input type="radio" name="stock" value="NSE Index" />NSE Index
            <input type="radio" name="stock" value="BSE Index" />BSE Index
            <input type="radio" name="stock" value="Gold Rate" />Gold Rate<br>
            
            <input type="submit" value="Submit" />
        </form>
    </body>
</html>
OUTPUT
 

   
   
   
PRACTICAL 4
Create a web service for UGC that contains a method which accepts college name as parameter and returns the NAAC rating. The college names and their ratings are stored in database. Design a web client to test the above web service.

CODE
RATINGS.JAVA
*()
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

**()
 *
 * @author patol
 */
@WebService(serviceName = "ratings")
public class ratings {

    /**
     * Web service operation
     */
    @WebMethod(operationName = "getrating")
    public String getratings(@WebParam(name = "college") String college) {
       String cname=null;
       try{
        Class.forName("org.apache.derby.jdbc.ClientDriver");
        Connection con=DriverManager.getConnection("jdbc:derby://localhost:1527/Collegeratings","user1","user1@123");
        Statement stmt=con.createStatement();
        ResultSet rs=stmt.executeQuery("SELECT * FROM COLLEGERATINGTABLE WHERE COLLEGENAME='"+college+"'");
        rs.next();
        cname=rs.getString("ADDRESS");
        rs.close();
        con.close();
        stmt.close();
    }
        catch(Exception e)
        {
            e.printStackTrace();
        }
    return cname;
   }

    }
CLIENT.JSP
<%-- 
    Document   : client
    Created on : 25 Jul, 2023, 9:18:05 PM
    Author     : patol
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
    
    <%
         String choice = request.getParameter("colleg");

    try {
	mypack.Ratings_Service service = new mypack.Ratings_Service();
	mypack.Ratings port = service.getRatingsPort();
	 // TODO initialize WS operation arguments here
	java.lang.String college = "";
	// TODO process result here
	java.lang.String result = port.getrating(choice);
	out.println("Result = "+result);
    } catch (Exception ex) {
	
    }
    get_ipython().run_line_magic('>', '')
   
 
    </body>
</html>
INDEX.HTML
<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <title>TODO supply a title</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <div></div>
        <form action="client.jsp">
            enter your colleges:-</br></br>
            <input type="text" name="colleg" value="" /><br></br>
            <input type="submit" value="submit" name="submit" /></br></br>
        </form>
    </body>
</html>
OUTPUT
 
 
     
PRACTICAL 5
Design a web service for a channel containing 2 functions – 1st function called getBreakingNews which accepts date as string parameter and returns special news of that day, 2nd function called getPrediction  accepts sunsign name as string parameter and returns predictions as string. Design a client to test the above web service.

CODE
NEWSCHANNEL.JAVA
*()
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

**()
 *
 * @author patol
 */
@WebService(serviceName = "newschannel")
public class newschannel {

    /**
     * Web service operation
     */
    @WebMethod(operationName = "getBreakingnews")
    public String getBreakingnews(@WebParam(name = "date") String date) {
         String cname=null;
       try{
        Class.forName("org.apache.derby.jdbc.ClientDriver");
        Connection con=DriverManager.getConnection("jdbc:derby://localhost:1527/user1","user1","user1@123");
        Statement stmt=con.createStatement();
        ResultSet rs=stmt.executeQuery("SELECT * FROM BREAKINGNEWS WHERE DATE='"+date+"'");
        rs.next();
        cname=rs.getString("NEWS");
        rs.close();
        con.close();
        stmt.close();
    }
        catch(Exception e)
        {
            e.printStackTrace();
        }
    return cname;
   }

    /**
     * Web service operation
     */
    @WebMethod(operationName = "getPrediction")
    public String getPrediction(@WebParam(name = "sunsignname") String sunsignname) {
         String cdname=null;
       try{
        Class.forName("org.apache.derby.jdbc.ClientDriver");
        Connection con=DriverManager.getConnection("jdbc:derby://localhost:1527/user2","user1","user1@123");
        Statement stmt=con.createStatement();
        ResultSet rs=stmt.executeQuery("SELECT * FROM PREDICTION WHERE SUNSIGNNAME='"+sunsignname+"'");
        rs.next();
        cdname=rs.getString("HOROSCOPE");
        rs.close();
        con.close();
        stmt.close();
    }
        catch(Exception e)
        {
            e.printStackTrace();
        }
    return cdname;
   }
    }
CLIENT.JSP
<%-- 
    Document   : client
    Created on : 26 Jul, 2023, 7:43:25 PM
    Author     : patol
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <%
       String choice=request.getParameter("newsdate");
           
    
    try {
	mypack.Newschannel_Service service = new mypack.Newschannel_Service();
	mypack.Newschannel port = service.getNewschannelPort();
	 // TODO initialize WS operation arguments here
	java.lang.String date = "";
	// TODO process result here
	java.lang.String result = port.getBreakingnews(choice);
	out.println("Result = "+result);
    } catch (Exception ex) {
	// TODO handle custom exceptions here
    }
    get_ipython().run_line_magic('>', '')
    </BR></BR>
    <%
        String choice2=request.getParameter("sunsign");
            
    try {
	mypack.Newschannel_Service service = new mypack.Newschannel_Service();
	mypack.Newschannel port = service.getNewschannelPort();
	 // TODO initialize WS operation arguments here
	java.lang.String sunsignname = "";
	// TODO process result here
	java.lang.String result = port.getPrediction(choice2);
	out.println("Result = "+result);
    } catch (Exception ex) {
	// TODO handle custom exceptions here
    }
    get_ipython().run_line_magic('>', '')
    </body>
</html>
INDEX.HTML
<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <title>NEWS CHANNEL</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <div>
            <form action="client.jsp">
                enter the date for which you need the news</br></br>
                <input type="text" name="newsdate" value="" /></br></br>
                enter your sun sign</br></br>
                <input type="text" name="sunsign" value="" /></br></br>
                <input type="submit" value="submit" /></br></br>
            </form>
        </div>
    </body>
</html>
OUTPUT
 
   
        

PRACTICAL 6
Design a Restful webservice from a database table Employee with columns empid,empname and Designation. Test the webservice for the various http requests

CODE
DATABASE TABLE EMPLOYEE

EMPLOYEEFACADEREST.JAVA
*()
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package mypack.service;

import java.util.List;
import javax.ejb.Stateless;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.ws.rs.Consumes;
import javax.ws.rs.DELETE;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.PUT;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import mypack.Employee;

**()
 *
 * @author patol
 */
@Stateless
@Path("mypack.employee")
public class EmployeeFacadeREST extends AbstractFacade<Employee> {

    @PersistenceContext(unitName = "PRACTICAL6_054PU")
    private EntityManager em;

    public EmployeeFacadeREST() {
        super(Employee.class);
    }

    @POST
    @Override
    @Consumes({MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON})
    public void create(Employee entity) {
        super.create(entity);
    }

    @PUT
    @Path("{id}")
    @Consumes({MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON})
    public void edit(@PathParam("id") String id, Employee entity) {
        super.edit(entity);
    }

    @DELETE
    @Path("{id}")
    public void remove(@PathParam("id") String id) {
        super.remove(super.find(id));
    }

    @GET
    @Path("{id}")
    @Produces({MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON})
    public Employee find(@PathParam("id") String id) {
        return super.find(id);
    }

    @GET
    @Override
    @Produces({MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON})
    public List<Employee> findAll() {
        return super.findAll();
    }

    @GET
    @Path("{from}/{to}")
    @Produces({MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON})
    public List<Employee> findRange(@PathParam("from") Integer from, @PathParam("to") Integer to) {
        return super.findRange(new int[]{from, to});
    }

    @GET
    @Path("count")
    @Produces(MediaType.TEXT_PLAIN)
    public String countREST() {
        return String.valueOf(super.count());
    }

    @Override
    protected EntityManager getEntityManager() {
        return em;
    }
    
}
OUTPUT
GET METHOD


POST METHOD(AFTER ADDING JAKE PERALTA,MANAGER,012)

CLIENT SIDE
CODE
EMPLOYEE.JSP
<%-- 
    Document   : employee
    Created on : 2 Sep, 2023, 4:45:49 PM
    Author     : patol
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
        <style>
            table{
                font-family: arial,sans-serif;
                border-collapse: collapse;
            }
            td,th{
                border:1px solid #000000;
                text-align:center;
                padding: 8px;
            }
        </style>
        <script>
            var request=new XMLHttpRequest();
            request.open('GET','http://localhost:8080/EmployeeRest/webresources/mypack.employee',true); //url from test web service parameter
            request.onload=function(){
                //data will hold http request
                var data=JSON.parse(this.response);
                for (var i=0;i<data.length;i++)
                {
                    var table=document.getElementById("emptable");
                    var row=table.insertRow();
                    var cell1=row.insertCell(0);
                    var cell2=row.insertCell(1);
                    var cell3=row.insertCell(2);
                    cell1.innerHTML=data[i].empid;
                    cell2.innerHTML=data[i].empname;
                    cell3.innerHTML=data[i].designation;
                }
            };
            request.send();
        </script>
    </head>
    <body>
       <table id="emptable">
            <tr>
                <th> Employee Id</th>
                <th>Employee Name</th>
                <th>Employee Designation</th>
            </tr>
        </table> 
    </body>
</html>
INDEX.HTML
<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <title>TODO supply a title</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
         <form>
             Get List of Employees<br><br>
            <input type="submit" formaction="employee.jsp" value="Get Employees"></br>
        </form>
    </body>
</html>
OUTPUT
 

PRACTICAL 7
Design a Restful webservice from a database table Student with columns rollno, name and totalmarks. Create a restful client that displays the data by accessing restful service.
CODE
DATABASE TABLE

STUDENTFACADEREST.JAVA
*()
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package mypack.service;

import java.util.List;
import javax.ejb.Stateless;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.ws.rs.Consumes;
import javax.ws.rs.DELETE;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.PUT;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import mypack.Student;

**()
 *
 * @author patol
 */
@Stateless
@Path("mypack.student")
public class StudentFacadeREST extends AbstractFacade<Student> {

    @PersistenceContext(unitName = "PRACTICAL7_054PU")
    private EntityManager em;

    public StudentFacadeREST() {
        super(Student.class);
    }

    @POST
    @Override
    @Consumes({MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON})
    public void create(Student entity) {
        super.create(entity);
    }

    @PUT
    @Path("{id}")
    @Consumes({MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON})
    public void edit(@PathParam("id") String id, Student entity) {
        super.edit(entity);
    }

    @DELETE
    @Path("{id}")
    public void remove(@PathParam("id") String id) {
        super.remove(super.find(id));
    }

    @GET
    @Path("{id}")
    @Produces({MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON})
    public Student find(@PathParam("id") String id) {
        return super.find(id);
    }

    @GET
    @Override
    @Produces({MediaType.APPLICATION_JSON})
    public List<Student> findAll() {
        return super.findAll();
    }

    @GET
    @Path("{from}/{to}")
    @Produces({MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON})
    public List<Student> findRange(@PathParam("from") Integer from, @PathParam("to") Integer to) {
        return super.findRange(new int[]{from, to});
    }

    @GET
    @Path("count")
    @Produces(MediaType.TEXT_PLAIN)
    public String countREST() {
        return String.valueOf(super.count());
    }

    @Override
    protected EntityManager getEntityManager() {
        return em;
    }
    
}

OUTPUT


CLIENT SIDE
CODE
CLIENT.JSP
<%-- 
    Document   : client
    Created on : 2 Sep, 2023, 5:20:13 PM
    Author     : patol
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
        <style>
            table{
                font-family: arial,sans-serif;
                border-collapse: collapse;
            }
            td,th{
                border:1px solid #000000;
                text-align:center;
                padding: 8px;
            }
        </style>
        <script>
            var request=new XMLHttpRequest();
            request.open('GET','http://localhost:8080/PRACTICAL7_054/webresources/mypack.student',true); //url from test web service parameter
            request.onload=function(){
                //data will hold http request
                var data=JSON.parse(this.response);
                for (var i=0;i<data.length;i++)
                {
                    var table=document.getElementById("stdtable");
                    var row=table.insertRow();
                    var cell1=row.insertCell(0);
                    var cell2=row.insertCell(1);
                    var cell3=row.insertCell(2);
                    cell1.innerHTML=data[i].rollno;
                    cell2.innerHTML=data[i].name;
                    cell3.innerHTML=data[i].totalmarks;
                }
            };
            request.send();
        </script>
    </head>
    <body>
        <table id="stdtable">
            <tr>
                <th> Roll Number</th>
                <th>Student Name</th>
                <th>Total Marks</th>
            </tr>
        </table>
    </body>
</html>

INDEX.HTML
<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <title>TODO supply a title</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <form action="client.jsp">
            get list of students<br><br>
            <input type="submit" value="press here for details" />
        </form>
    </body>
</html>
OUTPUT
        





PRACTICAL 8
Create a WCF service to perform calculations like Addition, Subtraction , Multiplication and Division. Create a client for WCF which invokes the various operations.
CODE
ISERVICE1.CS
using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.Text;

namespace CalculatorService
{
    // NOTE: You can use the "Rename" command on the "Refactor" menu to change the interface name "IService1" in both code and config file together.
    [ServiceContract]
    public interface IService1
    {
        [OperationContract]
        double Add(double num1, double num2);

        [OperationContract]
        double Subtract(double num1, double num2);

        [OperationContract]
        double Multiply(double num1, double num2);

        [OperationContract]
        double Divide(double num1, double num2);
    }
}
SERVICE1.SVC.CS
using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.Text;

namespace CalculatorService
{
    // NOTE: You can use the "Rename" command on the "Refactor" menu to change the class name "Service1" in code, svc and config file together.
    // NOTE: In order to launch WCF Test Client for testing this service, please select Service1.svc or Service1.svc.cs at the Solution Explorer and start debugging.
    public class Service1 : IService1
    {
        public double Add(double num1, double num2)
        {
            return num1 + num2;
        }

        public double Divide(double num1, double num2)
        {
            return num1 / num2;
        }

 

        public double Multiply(double num1, double num2)
        {
            return num1 * num2;
        }

        public double Subtract(double num1, double num2)
        {
            return num1 - num2;
        }
    }
}
DEFAULT.ASPX
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="ArithmeticClient.Default" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <br />
            <asp:TextBox ID="TextBox1" runat="server" OnTextChanged="TextBox1_TextChanged"></asp:TextBox>
&nbsp;&nbsp;
            <br />
            <br />
            <asp:TextBox ID="TextBox2" runat="server"></asp:TextBox>
            <br />
            <br />
            <br />
            <asp:TextBox ID="TextBox3" runat="server"></asp:TextBox>
            <br />
            <br />
            <br />
            <asp:Button ID="Button1" runat="server" OnClick="Button1_Click" Text="Sum" />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <asp:Button ID="Button2" runat="server" OnClick="Button2_Click" Text="Difference" />
            <br />
            <br />
            <asp:Button ID="Button3" runat="server" OnClick="Button3_Click" Text="Multiply" />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <asp:Button ID="Button4" runat="server" OnClick="Button4_Click" Text="Division" />
            <br />
            <br />
        </div>
    </form>
</body>
</html>
DEFAULT.ASPX.CS
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace ArithmeticClient
{
    public partial class Default : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void TextBox1_TextChanged(object sender, EventArgs e)
        {

        }

        protected void Button1_Click(object sender, EventArgs e)
        {
            ServiceReference1.Service1Client client = new ServiceReference1.Service1Client();
            double num1 = double.Parse(TextBox1.Text);
            double num2 = double.Parse(TextBox2.Text);
            TextBox3.Text = Convert.ToString(client.Add(num1, num2));
        }

        protected void Button2_Click(object sender, EventArgs e)
        {
            ServiceReference1.Service1Client client = new ServiceReference1.Service1Client();
            double num1 = double.Parse(TextBox1.Text);
            double num2 = double.Parse(TextBox2.Text);
            TextBox3.Text = Convert.ToString(client.Subtract(num1, num2));
        }

        protected void Button3_Click(object sender, EventArgs e)
        {
            ServiceReference1.Service1Client client = new ServiceReference1.Service1Client();
            double num1 = double.Parse(TextBox1.Text);
            double num2 = double.Parse(TextBox2.Text);
            TextBox3.Text = Convert.ToString(client.Multiply(num1, num2));
        }

        protected void Button4_Click(object sender, EventArgs e)
        {
            ServiceReference1.Service1Client client = new ServiceReference1.Service1Client();
            double num1 = double.Parse(TextBox1.Text);
            double num2 = double.Parse(TextBox2.Text);
            TextBox3.Text = Convert.ToString(client.Divide(num1, num2));
        }
    }
}
OUTPUT
DIVISION
 
SUBTRACTION
 
MULTIPLY
 

ADDITION
 
PRACTICAL 9
Create a WCF service with different endpoint for Soap based and Rest based implementation.

CODE
ISERVICE1.CS
using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.Text;

namespace WcfService2
{
    // NOTE: You can use the "Rename" command on the "Refactor" menu to change the interface name "IService1" in both code and config file together.
    [ServiceContract]
    public interface IService1
    {
        [OperationContract]
        [System.ServiceModel.Web.WebInvoke(Method = "GET", UriTemplate = "/SayHello/{value}", RequestFormat = System.ServiceModel.Web.WebMessageFormat.Json, ResponseFormat = System.ServiceModel.Web.WebMessageFormat.Json)]
        string SayHello(string value);

    }
    
    }
SERVICE1.SVC.CS
using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.Text;

namespace WcfService2
{
    // NOTE: You can use the "Rename" command on the "Refactor" menu to change the class name "Service1" in code, svc and config file together.
    // NOTE: In order to launch WCF Test Client for testing this service, please select Service1.svc or Service1.svc.cs at the Solution Explorer and start debugging.
    public class Service1 : IService1
    {

        public string SayHello(string value)
        {
            return string.Format($"hello {value}!!welcome to wcf");
        }
    }
}
WEB.CONFIG
<?xml version="1.0"?>
<configuration>

  <appSettings>
    <add key="aspnet:UseTaskFriendlySynchronizationContext" value="true" />
  </appSettings>
  <system.web>
    <compilation debug="true" targetFramework="4.7.2" />
    <httpRuntime targetFramework="4.7.2"/>
  </system.web>
  <system.serviceModel>
	  <services>
		  <service name="WcfService2.Service1">
			  <endpoint address="jsonservice" binding="webHttpBinding" contract="WcfService2.IService1" behaviorConfiguration="web">

			  </endpoint>
			  <endpoint address="soapservice" binding="basicHttpBinding" contract="WcfService2.IService1">

			  </endpoint>
		  </service>
	  </services>
    <behaviors>
      <serviceBehaviors>
        <behavior>
          <!-- To avoid disclosing metadata information, set the values below to false before deployment -->
          <serviceMetadata httpGetEnabled="true" httpsGetEnabled="true"/>
          <!-- To receive exception details in faults for debugging purposes, set the value below to true.  Set to false before deployment to avoid disclosing exception information -->
          <serviceDebug includeExceptionDetailInFaults="false"/>
        </behavior>
      </serviceBehaviors>
		<endpointBehaviors>
			<behavior name="web">
				<webHttp/>
			</behavior>
		</endpointBehaviors>
    </behaviors>
    <protocolMapping>
        <add binding="basicHttpsBinding" scheme="https" />
    </protocolMapping>    
    <serviceHostingEnvironment aspNetCompatibilityEnabled="true" multipleSiteBindingsEnabled="true" />
  </system.serviceModel>
  <system.webServer>
    <modules runAllManagedModulesForAllRequests="true"/>
    <!--
        To browse web app root directory during debugging, set the value below to true.
        Set to false before deployment to avoid disclosing web app folder information.
      -->
    <directoryBrowse enabled="true"/>
  </system.webServer>

</configuration>
OUTPUT
 

