<%-- 
    Document   : newjsp
    Created on : Jul 11, 2023, 11:09:47 AM
    Author     : cs3
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
    %>
 

        
    
  

    </body>
</html>
