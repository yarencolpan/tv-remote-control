import random


class RemoteControl:

    def __init__(self, tv_status="Off", volume_status=0, channel_list=["Bbc"], current_channel="Bbc"):
        self.tv_status = tv_status
        self.volume_status = volume_status
        self.channel_list = channel_list
        self.current_channel = current_channel

    def __str__(self):
        return "tv_status: {}\n" \
               "sound_status: {}\n" \
               "channel_list: {}\n" \
               "current_channel: {}".format(self.tv_status, self.volume_status, self.channel_list, self.current_channel)

    def __len__(self):
        return len(self.channel_list)

    def tv_on(self):
        if self.tv_status == "On":
            print("The Tv is on.")
        else:
            self.tv_status = "Off"
            print("The Tv is on.")

    def tv_off(self):
        if self.tv_status == "Off":
            print("The Tv is off.")
        else:
            self.tv_status = "Off"
            print("The Tv is off.")

    def raise_volume(self):
        if self.volume_status != 30:
            self.volume_status += 1
            print("new volume", self.volume_status)

    def lower_volume(self):
        if self.volume_status != 0:
            self.volume_status -= 1
            print("New volume is", self.volume_status)

    def adding_channel(self, name_channel):
        print("please wait......")
        self.channel_list.append(name_channel)
        print("channels is", self.channel_list)

    def change_channel(self):
        new_channel = random.randint(0, len(self.channel_list)-1)
        self.current_channel = self.channel_list[new_channel]
        print("new channel is", self.current_channel)


remote_control1 = RemoteControl()


print("""
Tv remote control

  -To learn about the tv status, volume status, channel list, and current channel, press '1'
  -To learn about channel count, press '2'
  -To turn on Tv, press '3'
  -To turn off Tv, press'4'
  -To raise the volume, press '5'
  -To lower the volume, press '6'
  -To adding channel, press '7'
  -To change the channel, press '8'
  -To exit, press '9'
""")

while True:
    operation = int(input("enter the number:"))
    if remote_control1 == 9:
        break

    elif operation == 1:
        print(remote_control1)

    elif operation == 2:
        print("Channel count:", len(remote_control1))

    elif operation == 3:
        remote_control1.tv_on()

    elif operation == 4:
        remote_control1.tv_off()

    elif operation == 5:
        remote_control1.raise_volume()

    elif operation == 6:
        remote_control1.lower_volume()

    elif operation == 7:
        tv_channels = input("write channels names with commas in between: ")
        additions = tv_channels.split(",")

        for i in additions:
            remote_control1.adding_channel(i)

    elif operation == 8:
        remote_control1.change_channel()

