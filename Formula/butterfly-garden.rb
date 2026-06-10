class ButterflyGarden < Formula
  desc "Animated butterfly garden in your terminal"
  homepage "https://github.com/sharmark9931/butterfly-garden"
  url "https://github.com/sharmark9931/butterfly-garden/archive/refs/tags/v1.0.1.tar.gz"
  sha256 "2e90c4adb22c5a8aa7f63efe21fa56bee409422cd9dbf7e1de24d017c4fef10d"
  license "MIT"

  # No compiled dependencies — uses whatever python3 is already on the system
  uses_from_macos "python3"

  def install
    libexec.install "butterfly.py"

    (bin/"butterfly").write <<~EOS
      #!/usr/bin/env python3
      import sys
      sys.path.insert(0, "#{libexec}")
      from butterfly import main_cli
      main_cli()
    EOS

    chmod 0755, bin/"butterfly"
  end

  test do
    assert_predicate bin/"butterfly", :exist?
    assert_match "main_cli", shell_output("grep main_cli #{libexec}/butterfly.py")
  end
end
