#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##practical 1


# In[ ]:





# In[ ]:


##practical 2


# In[ ]:


<%-- 
    Document   : client
    Created on : Jul 5, 2023, 9:46:25 AM
    Author     : cs26
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


# In[ ]:


##practical 3


# In[ ]:


sql query---
INSERT INTO USER1.STOCKDATA (NSE,BSE,GOLDRATE) VALUES(500,350,5500);


source code---
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


# In[ ]:


##practical 4


# In[ ]:


----SQL TABLE----
INSERT INTO USER1.COLLEGERATINGTABLE VALUES('SIES','B');
INSERT INTO USER1.COLLEGERATINGTABLE VALUES('MCC','A');
INSERT INTO USER1.COLLEGERATINGTABLE VALUES('KELKAR','A');
INSERT INTO USER1.COLLEGERATINGTABLE VALUES('KJ SOMAIYA','B');
INSERT INTO USER1.COLLEGERATINGTABLE VALUES('RUIA','A');
INSERT INTO USER1.COLLEGERATINGTABLE VALUES('HINDUJA','B');
----RATINGS.JAVA----
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
-----CLIENT.JSP----
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
-----INDEX.HTML-----
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
    


# In[ ]:


##practical 5


# In[ ]:


INSERT INTO USER1.BREAKINGNEWS VALUES('20 JULY','HEAVY RAINS');
INSERT INTO USER1.BREAKINGNEWS VALUES('21 JULY','WATER SHORTAGE');
INSERT INTO USER1.BREAKINGNEWS VALUES('22 JULY','THUNDERSTORMS');
INSERT INTO USER1.BREAKINGNEWS VALUES('23 JULY','SHOPS CLOSED');

INSERT INTO USER1.PREDICTION VALUES('ARIES','NO WORRIES');
INSERT INTO USER1.PREDICTION VALUES('GEMINI','STAY HYDRATED');
INSERT INTO USER1.PREDICTION VALUES('CAPRICORN','KEEP WORKING HARD');
INSERT INTO USER1.PREDICTION VALUES('SAGGITARIUS','STAY HAPPY');

--index.html--
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
       
        <form action="CLIENT.jsp">
            SELECT YOUR DATE:-</BR></BR>
            <input type="text" name="DATE" value="" /></BR>
            SELECT YOUR SUN SIGN:-</BR></BR>
            <input type="text" name="SUNSIGN" value="" /></BR></BR>
            <input type="submit" value="SUBMIT" name="SUBMIT" /></BR>
        </form>
    </body>
</html>
--client.jsp--
<%-- 
    Document   : CLIENT
    Created on : Jul 25, 2023, 11:14:14 AM
    Author     : sies
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
      String choice=request.getParameter("DATE");     
    try {
	mypack.Channel_Service service = new mypack.Channel_Service();
	mypack.Channel port = service.getChannelPort();
	 // TODO initialize WS operation arguments here
	java.lang.String date = "";
	// TODO process result here
	java.lang.String result = port.getBreakingNews(choice);
	out.println("Result = "+result);
    } catch (Exception ex) {
	// TODO handle custom exceptions here
    }
    get_ipython().run_line_magic('>', '')
 
    
    <%
        String choic=request.getParameter("SUNSIGN");
        try {
	mypack.Channel_Service service = new mypack.Channel_Service();
	mypack.Channel port = service.getChannelPort();
	 // TODO initialize WS operation arguments here
	java.lang.String sunsignname = "";
	// TODO process result here
	java.lang.String result = port.getPrediction(choic);
	out.println("Result = "+result);
    } catch (Exception ex) {
	// TODO handle custom exceptions here
    }
    get_ipython().run_line_magic('>', '')
    

         
      
    </body>
</html>
---channel.java---
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
 * @author sies
 */
@WebService(serviceName = "Channel")
public class Channel {

    /**
     * Web service operation
     */
    @WebMethod(operationName = "getBreakingNews")
    public String getBreakingNews(@WebParam(name = "date") String date) {
        String cname=null;
       try{
        Class.forName("org.apache.derby.jdbc.ClientDriver");
        Connection con=DriverManager.getConnection("jdbc:derby://localhost:1527/user2","user1","user1@123");
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
        ResultSet rs=stmt.executeQuery("SELECT * FROM PREDICTION WHERE SUNSIGN='"+sunsignname+"'");
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


# In[ ]:


##practical 6


# In[ ]:


----employee.jsp----
<%-- 
    Document   : employee
    Created on : Aug 8, 2023, 10:29:55 AM
    Author     : sies
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
            request.open('GET','http://localhost:18181/PRACTICAL6_054/webresources/mypack.empdata',true); //url from test web service parameter
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

----index.html-----
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
            <input type="submit" formaction="employee.jsp" value="Get Employees">get employees</br>
        </form>
    </body>
</html>


# In[ ]:


##practical 7


# In[ ]:





# In[ ]:


##practical 8


# In[ ]:





# In[ ]:


##practical 9


# In[ ]:


---------Service.cs-----------
using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.Text;

namespace WcfService1
{
    // NOTE: You can use the "Rename" command on the "Refactor" menu to change the interface name "IService1" in both code and config file together.
    [ServiceContract]
    public interface IService1
    {
        [OperationContract]
        [System.ServiceModel.Web.WebInvoke(Method = "GET", UriTemplate = "/SayHello/{value}",RequestFormat =System.ServiceModel.Web.WebMessageFormat.Json,ResponseFormat=System.ServiceModel.Web.WebMessageFormat.Json)]
        string SayHello(string value);
     
    }
}

---------Service1.svc.cs----------
using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.Text;

namespace WcfService1
{
    // NOTE: You can use the "Rename" command on the "Refactor" menu to change the class name "Service1" in code, svc and config file together.
    // NOTE: In order to launch WCF Test Client for testing this service, please select Service1.svc or Service1.svc.cs at the Solution Explorer and start debugging.
    public class Service1 : IService1
    {
       
        
public string SayHello(string value)
        {
            return string.Format($"helle {value}!! welcome to wcf");
        }
    }
}

-----------web.config--->changes-----------
<services>
		  <service name="WcfService1.Service">
			  <endpoint address="jsonservice" binding="webHttpBinding" contract="WcfService1.IService1" behaviorConfiguration="web"> 
				  
			  </endpoint>
			  <endpoint address="soapservice" binding="basicHttpBinding" contract="WcfService1.IService1">
				  
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
			</behavior>"
		</endpointBehaviors>
    </behaviors>
    
    
    web.config changes
    ------after </system.serviceModel>-------
<services>
		  <service name="WcfService1.Service">
			  <endpoint address="jsonservice" binding="webHttpBinding" contract="WcfService1.IService1" behaviorConfiguration="web"> 
				  
			  </endpoint>
			  <endpoint address="soapservice" binding="basicHttpBinding" contract="WcfService1.IService1">
				  
			  </endpoint>
		  </service>
	  </services>
-----after </serviceBehaviors>------
<endpointBehaviors>
			<behavior name="web">
				<webHttp/>
			</behavior>"
		</endpointBehaviors>
    

