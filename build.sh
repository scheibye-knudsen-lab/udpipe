docker build -t udpipe/server-da .
docker save udpipe/server-da > udpipe-server-da.rar
zip udpipe-server-da.rar.zip udpipe-server-da.rar
zip -s=1000m udpipe-server-da.rar.zip --out udpipe-server-da.rar.split.zip