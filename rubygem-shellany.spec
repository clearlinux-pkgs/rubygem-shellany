#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-shellany
Version  : 0.0.1
Release  : 1
URL      : https://rubygems.org/downloads/shellany-0.0.1.gem
Source0  : https://rubygems.org/downloads/shellany-0.0.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support

%description
# Shellany
Shellany captures command output.
## Features:
- portability (should work on recent JRuby versions)
- capturing stdout, stderr in a convenient way
- returning the result in a convenient way
- detecting if a shell is needed (though incomplete/primitive implementation)
- prevents running the same command multiple times

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n shellany-0.0.1
gem spec %{SOURCE0} -l --ruby > rubygem-shellany.gemspec

%build
gem build rubygem-shellany.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
shellany-0.0.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/shellany-0.0.1
rspec -I.:lib spec/ || :
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/shellany-0.0.1.gem
/usr/lib64/ruby/gems/2.2.0/doc/shellany-0.0.1/ri/Shellany/Sheller/_shellize_if_needed-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/shellany-0.0.1/ri/Shellany/Sheller/_system_with_capture-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/shellany-0.0.1/ri/Shellany/Sheller/_system_with_no_capture-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/shellany-0.0.1/ri/Shellany/Sheller/cdesc-Sheller.ri
/usr/lib64/ruby/gems/2.2.0/doc/shellany-0.0.1/ri/Shellany/Sheller/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/shellany-0.0.1/ri/Shellany/Sheller/ok%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/shellany-0.0.1/ri/Shellany/Sheller/ran%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/shellany-0.0.1/ri/Shellany/Sheller/run-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/shellany-0.0.1/ri/Shellany/Sheller/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/shellany-0.0.1/ri/Shellany/Sheller/status-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/shellany-0.0.1/ri/Shellany/Sheller/stderr-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/shellany-0.0.1/ri/Shellany/Sheller/stderr-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/shellany-0.0.1/ri/Shellany/Sheller/stdout-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/shellany-0.0.1/ri/Shellany/Sheller/stdout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/shellany-0.0.1/ri/Shellany/Sheller/system-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/shellany-0.0.1/ri/Shellany/cdesc-Shellany.ri
/usr/lib64/ruby/gems/2.2.0/doc/shellany-0.0.1/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/gems/shellany-0.0.1/.gitignore
/usr/lib64/ruby/gems/2.2.0/gems/shellany-0.0.1/.rspec
/usr/lib64/ruby/gems/2.2.0/gems/shellany-0.0.1/.travis.yml
/usr/lib64/ruby/gems/2.2.0/gems/shellany-0.0.1/Gemfile
/usr/lib64/ruby/gems/2.2.0/gems/shellany-0.0.1/LICENSE.txt
/usr/lib64/ruby/gems/2.2.0/gems/shellany-0.0.1/README.md
/usr/lib64/ruby/gems/2.2.0/gems/shellany-0.0.1/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/shellany-0.0.1/lib/shellany.rb
/usr/lib64/ruby/gems/2.2.0/gems/shellany-0.0.1/lib/shellany/sheller.rb
/usr/lib64/ruby/gems/2.2.0/gems/shellany-0.0.1/lib/shellany/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/shellany-0.0.1/shellany.gemspec
/usr/lib64/ruby/gems/2.2.0/gems/shellany-0.0.1/spec/lib/shellany/sheller_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/shellany-0.0.1/spec/shellany_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/shellany-0.0.1/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.2.0/specifications/shellany-0.0.1.gemspec
