# This script will increase the limit from 15 to 15000
exec { 'increase uLimit to 15000':
  path    => '/bin',
  command => "sed -i 's/15/15000/g' /etc/default/nginx",
}

exec { 'This will restart nginx':
  path    => '/usr/bin',
  command => 'service nginx restart',
}
