# configuring your server with Puppet
package { 'nginx':
  ensure  => installed,
  name    => 'nginx',
}

file { '/var/www/html/index.html':
  path    => '/var/www/html/index.html',
  content => 'Holberton School',
}

file { '/usr/share/nginx/html/index.html':
  content => 'Holberton School',
  path    => '/usr/share/nginx/html/index.html'
}

file { '/etc/nginx/sites-available/default':
  path  => '/etc/nginx/sites-available/default',
  content => 'server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
  }',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}