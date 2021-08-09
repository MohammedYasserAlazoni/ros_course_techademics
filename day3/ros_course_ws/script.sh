gnome-terminal --  roscore


source devel/setup.bash
gnome-terminal --  rosrun testing_pub_sub talker.py
gnome-terminal --  rosrun testing_pub_sub listener.py
