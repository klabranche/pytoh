# Visual Studio Code and GitHub Codespaces Example Using Python and Flask

This is a sample Python and Flask Application designed to show how easy it is to use Visual Studio Code and GitHub Codespaces.

The python code is of the [Tower of Hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi) puzzle that is often used to teach [recursion](https://en.wikipedia.org/wiki/Recursion) in computer science courses.

## What Is GitHub Codespaces

Your instant ready to go development box available anywhere, anytime, on any device with Visual Studio Code in the browser or on your machine with just a few extensions and nothing else.

The [presentation](presentation/GithubCodespaces.pdf) in the presentation folder gives a brief overview. 

### See it in action

To see it in action right now:

1. [Request access](https://github.com/features/codespaces/signup) to Codespaces for your github account.  Access should be given in a few hours.
1. After getting access to Codespaces, login to github and navigate to the https://github.com/klabranche/pytoh repository.
1. Select `Use this template`. While you can create a Codespace right from `<> code` this will create a copy of the repository in your profile.
1. Fill out the create a new repository from pytoh form and select `Create repository from template`.
1. On your new repository select the `<> Code` menu, select the `Codespaces` tab, then select the `Create codespace on main`.


### Running the Python Examples

If you don't already have your Codespace created and running then follow step 5 of the See it in action section and let it use the browser based version  of Visual Studio Code.

#### With Visual Studio Code In The Browser

With your Codespace now running:

1. In the terminal (CTRL+Shift+\`) type `python console.py` to run the command line version of the sample.
1. In the terminal type `flask run` and either click on the url in the text `* Running on http://127.0.0.1:5000 (Press CTRL+C to quit)` or select the `Open in Browser` in the popup message to run the web application version of the Tower Of Hanoi sample.
1. In the terminal press CTRL+C to stop the web application.
1. Close the tab that was running Visual Studio Code in the browser.

>:thumbsup: No installs, no setup and configuration.  It just ran.  That's what Codespaces with Visual Studio Code in the browser does for you.

#### With Visual Studio Code On Your Machine
If you want to use Visual Studio Code on your machine there are two extensions required:

* [GitHub Codespaces](https://marketplace.visualstudio.com/items?itemName=GitHub.codespaces)
* [Remote Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

If you don't install these extensions before trying to open in Visual Studio Code desktop the process will prompt you to.

If you haven't already logged into GitHub in Visual Studio Code you will be prompted to.

1. Re-open the Codespace by selecting the `<> Code` menu in your browser, select the `Codespaces` tab.
1. Select the randomly named Codespace and then `Open this codespace in VS Code desktop` when the Codespace page starts to load.
1. Select `Open` when you get the This site is trying to open Visual Studio Code.
1. Select `Open` when you get the Allow an extension to open this URI?

With your Codespace now running:

1. In the terminal (CTRL+Shift+\`), type `python console.py` to run the console version of the Tower of Hanoi sample.
1. In the terminal, type `flask run` and either click on the url in the text `* Running on http://127.0.0.1:5000 (Press CTRL+C to quit)` or select `Open in Browser` in the popup message to run the web application version of the Tower of Hanoi sample.
1. Press CTRL+C to stop the web application.
1. To stop the session, click `Codespaces` in the lower left hand corner of Visual Studio Code.  Select `Stop current codespace` in the drop down menu opened by the command palette.
 
### Debugging

You can debug with both the browser and desktop version of Visual Studio Code with Codespaces.

#### Debugging console.py 

1. Select `console.py` in the explorer (left hand icon menu).
1. Put a breakpoint on line 11 by clicking right to the left of the line number.
1. Select Run and Debug (left hand icon menu).
1. Select `Python: Current File` in the drop down menu at the top right of the Run and Debug window.
1. Press `F5` to start a debugging session.
1. At the prompt in the terminal enter something other than a number.
1. The breakpoint should now be hit.  Press `F5` to continue.

#### Debugging app.py (flask)

1. Select `app.py` in the explorer (left hand icon menu).
1. Put a breakpoint on line 9 by clicking right to the left of the line number.
1. Select Run and Debug (left hand icon menu).
1. Select `Python: Flask` in the drop down menu at the top right of the Run and Debug window.
1. Press `F5` to start a debugging session.
1. Either click on the url in the text `* Running on http://127.0.0.1:5000 (Press CTRL+C to quit)` or select `Open in Browser` in the popup message to run the web application version of the Tower of Hanoi sample.
1. The web page should now be spinning without anything showing yet.  That's because the breakpoint has been hit before we have returned the home page.
1. Press `F5` to continue and the home page should now load.
1. Press `Shift+F5` to end the debugging session.

### Sharing your app to others

By default the ports used by the container are private to your session only.  However, you can make it public to show your work to others.  This is ideal for a simple demo.  

>:exclamation: Don't do this for anything other than a demo.  This is not meant for production work or replacement of a server or web hosting.

1. Select `PORTS` tab that is in the terminal window.
1. Right click port 5000, select `Port Visibility` and then `Public`
1. Select `TERMINAL` tab again and then type at the command prompt `flask run`.

Now when you open the browser you will have a new url.  You can share this URL with others.

How is this working?  The GitHub Codespace is in the cloud and has setup this link to the outside world with the container.  Remember, the connection is to the container in the cloud not your local computer.

Let's go ahead and undo that now.  It's great for a quick pinch demo but we don't recommend it for much more than that.  

1. Select `PORTS` tab that is in the terminal window.
1. Right click port 5000, select `Port Visibility` and then `Private`

### Cleanup

You can delete the Codespace in GitHub or in Visual Studio Code.

>:warning: Deleting a Codespace deletes all work that was being done in the container.  Be sure to `push` your changes up to GitHub before deleting a Codespace.

#### Deleting Codespace using GitHub
1. Select the `<> Code` menu
1. Select `manage all`.  
1. For each Codespace in the list of Codespaces you want to delete select `...` menu and then select `Delete`.

#### Deleting Codespace using Visual Studio Code
1. Click `Codespaces` in the lower left hand corner of Visual Studio Code. 
1. Select `Delete Codespace` in the drop down menu opened by the command palette.
1. Select the codespace you want to delete from the drop down list.
1. Select `delete` when asked to confirm deletion.

### What Next

There is so much more to learn about Visual Studio Code and GitHub Codespaces. To learn more check out [GitHub Codespaces docs](https://docs.github.com/en/codespaces).

[Learn more about Flask](https://flask.palletsprojects.com/en/2.1.x/quickstart/#a-minimal-application)

[Deploy a Flask app to Azure](https://docs.microsoft.com/en-us/azure/app-service/quickstart-python?toc=%2Fazure%2Fdeveloper%2Fpython%2Ftoc.json&bc=%2Fazure%2Fdeveloper%2Fbreadcrumb%2Ftoc.json&tabs=flask%2Cwindows%2Cazure-portal%2Cterminal-bash%2Cvscode-deploy%2Cdeploy-instructions-azportal%2Cdeploy-instructions-zip-azcli) 

