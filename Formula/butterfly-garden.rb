class ButterflyGarden < Formula
  desc "Animated butterfly garden in your terminal"
  homepage "https://github.com/YOUR_GITHUB_USERNAME/butterfly-garden"
  # UPDATE the url and sha256 after you push a release tag on GitHub:
  #   curl -L https://github.com/YOUR_GITHUB_USERNAME/butterfly-garden/archive/refs/tags/v1.0.0.tar.gz | shasum -a 256
  url "https://github.com/YOUR_GITHUB_USERNAME/butterfly-garden/archive/refs/tags/v1.0.0.tar.gz"
  sha256 "REPLACE_WITH_SHA256_OF_YOUR_RELEASE_TARBALL"
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
