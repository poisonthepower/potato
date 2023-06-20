apt install sudo -y
apt install curl -y
apt install nano -y
apt install git -y
sudo apt install software-properties-common -y
add-apt-repository ppa:openjdk-r/ppa
apt-get update

mkdir ~/bin

PATH=~/bin:$PATH

cd ~/bin

curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo

chmod a+x ~/bin/repo

git clone https://github.com/akhilnarang/scripts.git scripts

cd scripts

bash setup/android_build_env.sh

cd
mkdir ev 
cd ev
git config --global user.name kibria5 && git config --global user.email mdkibria687@gmail.com

# Initialize local repository
repo init -u https://github.com/Evolution-X/manifest -b tiramisu
# Sync
repo sync -c -j$(nproc --all) --force-sync --no-clone-bundle --no-tags

git clone https://github.com/kibria5/device_xiaomi_violet.git -b 13 device/xiaomi/violet

echo "Stuffs to rm -rf"
rm -rf hardware/qcom-caf/sm8150/audio
rm -rf hardware/qcom-caf/sm8150/media
rm -rf hardware/qcom-caf/sm8150/display
rm -rf packages/resources/devicesettings

echo "Cloning Hals"
git clone --depth 1 https://github.com/SuperiorOS/android_hardware_qcom_audio.git -b thirteen-caf-sm8150  hardware/qcom-caf/sm8150/audio
git clone --depth 1 https://github.com/SuperiorOS/android_hardware_qcom_media.git -b twelve-caf-sm8150 hardware/qcom-caf/sm8150/media
git clone --depth 1 https://github.com/SuperiorOS/android_hardware_qcom_display.git -b twelve-caf-sm8150 hardware/qcom-caf/sm8150/display
git clone --depth 1 https://github.com/LineageOS/android_packages_resources_devicesettings -b lineage-20.0 packages/resources/devicesettings

echo "Cloning Vendor tree"
git clone --depth 1 https://github.com/kibria5/android_vendor_xiaomi_violet.git -b thirteen vendor/xiaomi/violet

echo "Cloning Kernel tree"
git clone --depth 1 https://github.com/kibria5/android_kernel_xiaomi_violet.git -b thirteen kernel/xiaomi/violet

echo "Firmware tree"
git clone --depth 1 https://gitlab.pixelexperience.org/android/vendor-blobs/vendor_xiaomi-firmware.git -b thirteen vendor/xiaomi-firmware

echo "Cloning MiuiCamera tree"
git clone --depth 1 https://gitlab.com/kibria5/android_vendor_miuicamera.git -b thirteen vendor/MiuiCamera

echo "Cloning Dolby Tree"
git clone --depth 1 https://github.com/danhancach/vendor_dolby.git -b dolby-1.0-d1 vendor/dolby

echo "Cloning Proton clang"
git clone --depth 1 https://github.com/kdrag0n/proton-clang.git -b master prebuilts/clang/host/linux-x86/clang-proton


# Set up environment
 . build/envsetup.sh

# Choose a target
lunch evolution_violet-userdebug

# Build the code
mka evolution

