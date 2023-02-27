# github-actions-udemy

# Installing .Net Console
1. Download .NET Core SDK
   - Visit the .NET Core download page (https://dotnet.microsoft.com/download) and download the appropriate SDK for your system.
   - Once the download is complete, double-click on the downloaded file and follow the installation instructions.

2. Open a Command Prompt
   - Open a new Command Prompt window by clicking on the Start menu and searching for "Command Prompt".

3. Create a new Console Application
   - To create a new console application, navigate to the directory where you want to create the project and run the following command:
   
     ```
     dotnet new console -o myApp
     ```
     
     This will create a new console application in a new directory named `myApp`. The `-o` option specifies the name of the output directory.

4. Build and Run the Application
   - Navigate to the newly created directory using the following command:
   
     ```
     cd myApp
     ```
     
   - To build and run the application, use the following commands:
   
     ```
     dotnet build
     dotnet run
     ```
     
     The `dotnet build` command will build the application and generate the necessary files. The `dotnet run` command will run the application.

That's it! You have successfully installed .NET Core and created a new console application. You can now open the project in your favorite editor (such as Visual Studio Code or Visual Studio) and start writing your application code.
