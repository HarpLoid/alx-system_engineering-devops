# A manifest that kills a process called killmenow

exec { 'pkill killmenow':
  command => '/usr/bin/pkill -f /killmenow',
}
