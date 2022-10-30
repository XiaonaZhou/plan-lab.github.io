---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# <i class="fas fa-users"></i>Team

{% include section.html %}
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: pi"
%}
{%
  include list.html
  data="members"
  component="portrait"
  filters="description: Ph.D. Student"
%}
{%
  include list.html
  data="members"
  component="portrait"
  filters="description: M.S. Student"
%}
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: undergrad"
%}
{:.center}

{% include section.html %}
# Alumni
{%
  include list.html
  data="members"
  component="portrait"
  filters="description: Alumni"
%}
{:.center}