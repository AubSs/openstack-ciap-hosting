tmux new-session \; \
  split-window -h \; \
  split-window -v \; \
  select-pane -t 1 \; \
  send-keys 'htop' C-m \; \
  select-pane -t 2 \; \
  resize-pane -U 25 \;
