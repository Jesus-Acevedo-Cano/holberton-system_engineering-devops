# using Puppet to make changes to our configuration file
file_line {'add identity file':
  path  => '/etc/ssh/ssh_config',
  line   => ' IdentityFile ~/.ssh/holberton',
  ensure => 'present',
}
file_line {'change pswrd aut':
  path  => '/etc/ssh/ssh_config',
  line   => ' PasswordAuthentication no',
  match => 'PasswordAuthentication yes',
  ensure => 'present',
}