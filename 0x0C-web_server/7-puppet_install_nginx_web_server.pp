# configuring your server with Puppet
package { 'nginx':
  ensure  => installed,
  name    => 'nginx',
}

file { 'index.html':
  path    => '/var/www/html/index.html',
  content => 'Holberton School',
}

file_line { 'redirect_me':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  after    => 'server_name _;',
  line     => 'rewrite ^/redirect_me return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;',
  multiple => true,
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}