# Visual Studio Code and GitHub Codespaces Example Using Python and Flask

This is a sample Python and Flask Application designed to show how easy it is to use Visual Studio Code and GitHub Codespaces.

The python code is of the [Tower of Hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi) puzzle that is often used to teach [recursion](https://en.wikipedia.org/wiki/Recursion) in computer science courses.

## What Is GitHub Codespaces

Your instant ready to go development box available anywhere, anytime, on any device with Visual Studio Code in the browser or on your machine with just a few extensions and nothing else.

The [presentation](presentation/GithubCodespaces.pdf) in the presentation folder gives a brief overview. 

### See it in action

To see it in action right now:

1. [Request access](https://github.com/features/codespaces) to Codespaces for your github account.  Access should be given in a few hours.
1. After getting access to Codespaces, login to github and then navigate to the https://github.com/klabranche/pytoh repository.
1. Select `Use this template`.
1. Fill out the create a new repository from pytoh form and select `Create repository from template`.
1. On your new repository select the `<> Code` menu, select the `Codespaces` tab, then select the `Create codespace on main`.


### Running the Python Examples

If you don't already have your Codespace created and running then follow step 5 of the See it in action section and let it use the browser based version  of Visual Studio Code.

With your Codespace now running:

1. In the terminal (CTRL+Shift+\`), type `python console.py` to run the console version of the Tower of Hanoi sample.
1. In the terminal, type `flask run` and either click on the url in the text `* Running on http://127.0.0.1:5000 (Press CTRL+C to quit)` or select the `Open in Browser` in the popup message to run the web application version of the Tower Of Hanoi sample.
1. Press CTRL+C to stop the web application.
1. Close the tab that was running Visual Studio Code in the browser.

>No installs, no setup and configuration.  It just ran.  That's what Codespaces with Visual Studio Code in the browser does for you.

If you want to use Visual Studio Code on your machine there are a few Extensions required:

[GitHub Codespaces](https://marketplace.visualstudio.com/items?itemName=GitHub.codespaces)

[Remote Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

If you don't install these extensions before trying to open in Visual Studio Code desktop the process will prompt you to.

If you haven't already logged into GitHub in Visual Studio Code you will be prompted to.

1. Re-open the Codespace by selecting the `<> Code` menu in your browser, select the `Codespaces` tab.
1. Select the randomly named Codespace and then `Open this codespace in VS Code desktop` when the Codespace page starts to load.
1. Select `Open` when you get the This site is trying to open Visual Studio Code.
1. Select `Open` when you get the Allow an extension to open this URI?

With your Codespace now running:

1. In the terminal (CTRL+Shift+\`), type `python console.py` to run the console version of the Tower of Hanoi sample.
1. In the terminal, type `flask run` and either click on the url in the text `* Running on http://127.0.0.1:5000 (Press CTRL+C to quit)` or select the `Open in Browser` in the popup message to run the web application version of the Tower of Hanoi sample.
1. Press CTRL+C to stop the web application.
1. To stop the session, click `Codespaces` in the lower left hand corner of Visual Studio Code.  Select `Stop current codespace` in the drop down menu opened by the command palette.
 
### Cleanup

You can delete the Codespace in GitHub or in Visual Studio Code.

#### Deleting Codespace using GitHub
1. Select the `<> Code` menu
1. Select `manage all`.  
1. For each Codespace in the list of Codespaces you want to delete select `...` menu and then select `Delete`.

#### Deleting Codespace using Visual Studio Code
1. Click `Codespaces` in the lower left hand corner of Visual Studio Code. 1. Select `Delete Codespace` in the drop down menu opened by the command palette.
1. Select the codespace you want to delete from the drop down list.
1. Select `delete` when asked to confirm deletion.

:warning: Deleting a Codespace deletes all work that was being done in the container.  Be sure to `push` your changes up to GitHub before deleting a Codespace.