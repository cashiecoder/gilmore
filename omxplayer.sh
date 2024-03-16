cd /usr/lib/arm-linux-gnueabihf
ln -s libmmal_core.so.0 libmmal_core.so
ln -s libmmal_util.so.0 libmmal_util.so
ln -s libmmal_vc_client.so.0 libmmal_vc_client.so
ln -s libbcm_host.so.0 libbcm_host.so
ln -s libvcsm.so.0 libvcsm.so
ln -s libvchiq_arm.so.0 libvchiq_arm.so
ln -s libvcos.so.0 libvcos.so
sudo curl -sSfLO 'https://raw.githubusercontent.com/raspberrypi/firmware/oldstable/opt/vc/lib/libbrcmEGL.so'
sudo curl -sSfLO 'https://raw.githubusercontent.com/raspberrypi/firmware/oldstable/opt/vc/lib/libbrcmGLESv2.so'
sudo curl -sSfLO 'https://raw.githubusercontent.com/raspberrypi/firmware/oldstable/opt/vc/lib/libopenmaxil.so'

git clone https://github.com/popcornmix/omxplayer.git
cd omxplayer
./prepare-native-raspbian.sh
make ffmpeg
make -j$(nproc)
sudo make install