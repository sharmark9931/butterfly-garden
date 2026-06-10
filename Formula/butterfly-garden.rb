class ButterflyGarden < Formula
  desc "Animated butterfly garden in your terminal"
  homepage "https://github.com/sharmark9931/butterfly-garden"
  url "https://github.com/sharmark9931/butterfly-garden/archive/refs/tags/v1.0.1.tar.gz"
  sha256 "2e90c4adb22c5a8aa7f63efe21fa56bee409422cd9dbf7e1de24d017c4fef10d"
  license "MIT"

  def install
    bin.install "butterfly.py" => "butterfly"
  end

  test do
    assert_predicate bin/"butterfly", :exist?
  end
end
