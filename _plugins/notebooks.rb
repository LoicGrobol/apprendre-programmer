module Jekyll
   class NotebookBadges < Liquid::Tag
      def initialize(tag_name, notebook_path, tokens)
         super
         @notebook_path = notebook_path.strip
         @notebook_path_escaped = ERB::Util.url_encode(@notebook_path)
      end
  
      def render(context)
         return "[![Open in Jupyterlite badge](#{context['site']['url']}#{context['site']['baseurl']}/assets/badge-launch.svg)](#{context['site']['url']}#{context['site']['baseurl']}/jupyterlite/notebooks/index.html?path=#{@notebook_path_escaped})"
      end
   end
end

Liquid::Template.register_tag('notebook_badges', Jekyll::NotebookBadges)