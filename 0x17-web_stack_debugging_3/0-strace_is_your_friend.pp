exec { '.phpp to .php':
  path => '/bin',
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
}
