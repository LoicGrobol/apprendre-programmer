module Jekyll
   class NotebookBadges < Liquid::Tag
      def initialize(tag_name, notebook_path, tokens)
         super
         @notebook_path = notebook_path.strip
      end
  
      def render(context)
          return "" # Temp hotfix
          binder_host = context['site'].fetch("binder_host", "https://mybinder.org")
          if context['site'].key?("environ_repository")
            repo_dir = context['site']['repository'].split("/").last
            if @notebook_path.end_with?(".md")
               notebook_path = @notebook_path + "?factory=Jupytext+Notebook"
            else
               notebook_path = @notebook_path
            end
            urlpath = (
               "?repo=#{ERB::Util.url_encode("https://github.com/" + context['site']['repository'])}" +
               "&urlPath=#{ERB::Util.url_encode("notebooks/#{repo_dir}/#{notebook_path}")}" +
               "&branch=#{context['site']['repo_branch']}"
            )
            urlpath_escaped = ERB::Util.url_encode(urlpath)
            res = (
               "[![Launch in Binder badge](#{binder_host}/badge_logo.svg)]" +
               "(#{binder_host}/v2/gh/#{context['site']['environ_repository']}/#{context['site']['repo_branch']}" +
               "?urlpath=git-pull#{urlpath_escaped})"
            )
         else
            res = "[![Launch in Binder badge](#{binder_host}/badge_logo.svg)](#{binder_host}/v2/gh/#{context['site']['repository']}/#{context['site']['repo_branch']}?urlpath=tree/#{@notebook_path})"
         end
         return res
      end
   end
end

module Jekyll
   class NotebookLink < Liquid::Tag
      def initialize(tag_name, notebook_path, tokens)
         super
         @notebook_path = notebook_path
      end
  
      def render(context)
         binder_host = context['site'].fetch("binder_host", "https://mybinder.org")
         res = "[![Launch in Binder badge](#{binder_host}/badge_logo.svg)]#{binder_host}/v2/gh/#{context['site']['repository']}/#{context['site']['repo_branch']}?urlpath=tree/#{@notebook_path})"
         return res
      end
   end
end

Liquid::Template.register_tag('notebook_badges', Jekyll::NotebookBadges)