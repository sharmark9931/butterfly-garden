class ButterflyGarden < Formula
  desc "Animated butterfly garden in your terminal"
  homepage "https://github.com/sharmark9931/butterfly-garden"
  url "https://github.com/sharmark9931/butterfly-garden/archive/refs/tags/v1.0.0.tar.gz"
  sha256 "2edc41e587cd9d157fd02570a3ae53a61ca8f9a6d698c419e2c10e7f516355c5"
  license "MIT"

  depends_on "python@3.11"

  def install
    # install butterfly.py as an executable script
    (bin/"butterfly").write <<~EOS
      #!/bin/bash
      exec "#{Formula["python@3.11"].opt_bin}/python3" "#{libexec}/butterfly.py" "$@"
    EOS
    libexec.install "butterfly.py"
  end

  test do
    # just verify the script is importable (curses needs a tty so we don't run it)
    system Formula["python@3.11"].opt_bin/"python3", "-c", "import butterfly"
  end
end
