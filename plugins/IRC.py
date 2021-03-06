class IRC:
    options = None
    writeFile = None

    def onEnable(self, parser, pluginloader):
        parser.add_option("-q", "--irc-out-file", dest="ircDump", default="ircdump.txt",
            help="file to dump messages to")

    def onDisable(self):
        if (self.writeFile != None):
            self.writeFile.close()

    def optionsParsed(self, parsedOptions):
        self.options = parsedOptions
        if (self.options.ircDump):
            self.writeFile = open(self.options.filename, 'w')
