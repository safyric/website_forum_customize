<?xml version="1.0" encoding="utf-8"?>

<odoo>
    <data>
        <template id="website_forum.forum_index_inherit" inherit_id="website_forum.forum_index">
            <xpath expr="//t[@t-esc='question_count']" position="replace"/>
            <xpath expr="//small[@class='dropdown']" position="replace">
                <small class="dropdown" t-if="filters in ('all', 'unanswered','followed', 'tag')">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                        <!--<t t-if="filters == 'unanswered'"> Unanswered</t>-->
                        <t t-if="filters == 'followed'"> Followed</t>
                        <t t-if="tag"> <span t-field="tag.name"/></t>
                        <t t-if="sorting == 'relevancy desc'"> by relevance</t>
                        <t t-if="sorting == 'write_date desc'"> by date</t>
                        <t t-if="sorting == 'create_date desc'"> by newest</t>
                        <!--<t t-if="sorting == 'child_count desc'"> by most answered</t>
                        <t t-if="sorting == 'vote_count desc'"> by most voted</t>-->
                        <b class="caret"/>
                    </a>
                    <ul class="dropdown-menu">
                        <li class="dropdown-header">Filter on</li>
                        <li t-att-class="filters == 'all' and 'active' or None ">
                            <a t-att-href="url_for('') + '?' + keep_query( 'search', 'sorting', filters='all')">All</a>
                        </li>
                        <!--<li t-att-class="filters == 'unanswered' and 'active' or None ">
                            <a t-att-href="url_for('') + '?' + keep_query( 'search', 'sorting', filters='unanswered')">Unanswered</a>
                        </li>-->
                        <li t-if="uid" t-att-class="filters == 'followed' and 'active' or None ">
                            <a t-att-href="url_for('') + '?' + keep_query( 'search', 'sorting', filters='followed')">Followed</a>
                        </li>
                        <li t-if="tag" class="dropdown-header">Tags</li>
                        <li t-if="tag" t-att-class="tag and 'active' or None ">
                            <a href=""><t t-esc="tag.name"/></a>
                        </li>
                        <li class="dropdown-header">Sort by</li>
                        <li t-att-class="sorting == 'relevancy desc' and 'active' or None ">
                            <a t-att-href="url_for('') + '?' + keep_query( 'search', 'filters', sorting='relevancy desc')">Relevance</a>
                        </li>
                        <!--<li t-att-class="sorting == 'write_date desc' and 'active' or None ">
                            <a t-att-href="url_for('') + '?' + keep_query( 'search', 'filters', sorting='write_date desc')">Last activity date</a>
                        </li>-->
                        <li t-att-class="sorting == 'create_date desc' and 'active' or None ">
                            <a t-att-href="url_for('') + '?' + keep_query( 'search', 'filters', sorting='create_date desc')">Newest</a>
                        </li>
                        <!--<li t-att-class="sorting == 'child_count desc' and 'active' or None ">
                            <a t-att-href="url_for('') + '?' + keep_query( 'search', 'filters', sorting='child_count desc')">Most answered</a>
                        </li>
                        <li t-att-class="sorting == 'vote_count desc' and 'active' or None ">
                            <a t-att-href="url_for('') + '?' + keep_query( 'search', 'filters', sorting='vote_count desc')">Most voted</a>
                        </li>-->
                    </ul>
                </small>
            </xpath>
        </template>
    </data>
</odoo>
