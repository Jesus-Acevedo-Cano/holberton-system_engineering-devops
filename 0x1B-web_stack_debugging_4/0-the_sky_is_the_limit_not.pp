# Fix failed requests
exec { 'fix--for-nginx':
  command  => "sed -i 's/-n 15/3000/g' /etc/default/nginx; service nginx restart",
  provider => 'shell',
}
