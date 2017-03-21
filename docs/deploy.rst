Travis-ci Automatic Deploy to Dokku
-----------------------------------


1. Generate new ssh-key without password - Give a name to the file.
2. Copy new ssh-key to your project (you must be in your root project)
3. Install Travis CI Command Line Client
4. Login to travis
5. Encrypt new ssh key with travis and copy the command to decrypt in terminal
6. Edit .travis.yml
7. add ssh-key to dokku server (go to Add ssh-key to dokku section)

http://tannguyen.org/2017/02/set-up-hugo-dokku-and-travis/

Terminal::

    $ ssh-keygen -t rsa
    $ cp ~/.ssh/<ssh name> ./deploy_utils/deploy_key
    $ sudo gem install travis
    $ travis login
    $ travis encrypt-file deploy_utils/deploy_key
    ->[.travis.yml] add before install:
        before_install:
          - openssl aes-256-cbc -K $encrypted_5d3fad67a2c7_key -iv $encrypted_5d3fad67a2c7_iv -in deploy_utils/deploy_key.enc -out deploy_utils/deploy_key -d
          (this command should be given after run travis encrypt-file [...]
    ->[.travis.yml] add after script:
        after_success:
          - eval "$(ssh-agent -s)" #start the ssh agent
          - chmod 600 deploy_utils/deploy_key # this key should have push access
          - ssh-add deploy_utils/deploy_key
          - git remote add deploy <git-remote>
          - git push deploy

Errors:
1. installing travis via `sudo gem install travis`

    ERROR:  Error installing travis:
    ERROR: Failed to build gem native extension.

Solution
- https://github.com/travis-ci/travis.rb/issues/391 ::

 sudo apt-get install python-software-properties
 sudo apt-add-repository ppa:brightbox/ruby-ng
 sudo apt-get update
 sudo apt-get install ruby2.1 ruby-switch
 sudo ruby-switch --set ruby2.1
 sudo apt-get install ruby2.1-dev


Add ssh-key to dokku
---------------------

1. Create a ssh-key
2. send ssh-key to server


Terminal::

    ssh-keygen -t rsa
    cat <path to ssh-key> | ssh root@<your.ip.address> "sudo sshcommand acl-add dokku [description]"
