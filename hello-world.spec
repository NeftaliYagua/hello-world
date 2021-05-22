Summary: Hello World!
Name: hello-world
Version: 1.0
Release: 1
License: GPL
Group: Applications/Productivity
#Source: https://github.com/NeftaliYagua/hello-world/archive/refs/tags/v1.0.zip
URL: https://github.com/NeftaliYagua/hello-world/
Vendor: Neftali Yagua
Packager: Neftalí Yagua <despacho@neftaliyagua.com>

%description
This is the hello world for testing purposes!

%build
wget https://github.com/NeftaliYagua/hello-world/releases/download/v1.0/hello-world-1.0-SNAPSHOT.jar
cat > hello-world.sh <<EOF
#!/usr/bin/bash
java -cp /usr/lib/hello-world/hello-world.jar com.neftaliyagua.HelloWorld.App
EOF

%install
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/lib/hello-world/
install -m 755 hello-world-1.0-SNAPSHOT.jar %{buildroot}/usr/lib/hello-world/hello-world.jar
install -m 755 hello-world.sh %{buildroot}/usr/bin/hello-world

%files
/usr/bin/hello-world
/usr/lib/hello-world/hello-world.jar
