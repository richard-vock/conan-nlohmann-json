from conans import ConanFile, CMake, tools


class NLohmannJSONConan(ConanFile):
    name = "nlohmann-json"
    version = "3.7.3"
    license = "LLVM"
    author = "Richard Vock <vock@cs.uni-bonn.de>"
    url = "https://github.com/richard-vock/conan-nlohmann-json"
    description = "JSON for Modern C++ (https://nlohmann.github.io/json/)"
    topics = ("json", "parser")
    settings = "os"

    def source(self):
        git = tools.Git(folder='nlohmann')
        git.clone("https://github.com/nlohmann/json.git", "v3.7.3")

    def package(self):
        self.copy("*.hpp", dst="include/nlohmann", src="nlohmann/include/nlohmann", keep_path=True)

    def package_id(self):
        self.info.header_only()

