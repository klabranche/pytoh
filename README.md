# Visual Studio Code and GitHub Codespaces Example Using Python and Flask

This is a sample Python and Flask Application designed to show how easy it is to use Visual Studio Code and GitHub Codespaces.

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

With your codespace now running:

1. In the terminal, type `python console.py` to run the console version of the Towers Of Hanoi sample.
1. In the terminal, type `flask run` and either click on the url in the text `* Running on http://127.0.0.1:5000 (Press CTRL+C to quit)` or select the `Open in Browser` in the popup message to run the web application version of the Towers Of Hanoi sample.
1. Press CTRL+C to stop the web application.
1. Close the tab that was running Visual Studio Code in the browser.

No installs, no setup and configuration.  It just ran.  That's what Codespaces with Visual Studio Code in the browser does for you.

If you want to use your Visual Studio Code on your machine.

Visual Studio Code requires the following Extensions for GitHub Codespaces:

[GitHub Codespaces](https://marketplace.visualstudio.com/items?itemName=GitHub.codespaces)
[Remote Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

If you don't install these extensions before hand, the process will ask you to.

1. Re-open the Codespace by selecting the `<> Code` menu in your browser, select the `Codespaces` tab.
1. Select the randomly named Codespace and then `Open this codespace in VS Code desktop` when the Codespace page starts to load.
1. Select `Open` when you get the This site is trying to open Visual Studio Code.
   1. If you haven't already installed the required Visual Studio Code Extensions you will be prompted to.
   1. If you haven't logged into GitHub in Visual Studio Code you will be prompted to.
1. Select `Open` when you get the Allow an extension to open this URI?
1.  