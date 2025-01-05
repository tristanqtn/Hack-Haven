# Kali Containers

```bash
docker run -d \
--name=kali-linux \
--security-opt seccomp=unconfined '#optional' \
-e PUID=1000 \
-e PGID=1000 \
-e TZ=Etc/UTC \
-e SUBFOLDER=/ '#optional' \
-e TITLE="Kali Linux" '#optional' \
-p 3000:3000 \
-p/3001:3001 \
--device /dev/dri:/dev/dri '#optional' \
--shm-size="1gb" '#optional' \
--restart unless-stopped \
lscr.io/linuxserver/kali-linux:latest
```
