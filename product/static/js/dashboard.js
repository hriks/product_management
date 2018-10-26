$(document).ready(() => {
    _p = new ProductManagement()
})
class ProductManagement {
    constructor () {
        this.categories_api = '/categories'
        this.subcategories_api = '/subcategories'
        this.product_api = '/products/'
        this.addContainer = $('#add_form_container')
        this.dataContainer = $('#tableData')
        this.addbuttonContainer = $('#add_btn_container')
        setTimeout(() => {
            this.updateProducts(ProductManagement.send_xml_request("GET", this.product_api)[0])
        })
    }

    updateProducts(details) {
        var resp = ''
        for (let index=0; index < details.length; index++) {
            resp += ProductManagement.getRowTemplate(details[index])
        }
        this.dataContainer.html(resp)
        this.cancel()
    }

    addProductForm() {
        var res = '<tr>'
        res += '<td colspan="4"><form onsubmit="return _p.addProduct();">'
        res += '<div class="row">'
        res += '<div class="col-sm-1">'
        res += '<button type="submit" class="btn btn-default">Save</button>'
        res += '<br><span onclick=_p.cancel()>Cancel</span></div>'
        res += '<div class="col-sm-4"><input type="text" placeholder="Product Name here" required id="product"></div>'
        res += '<div class="col-sm-3"><select required id="sub_category"><option value="">Select Sub Category</option></select></div>'
        res += '<div class="col-sm-3"><select required id="category"><option value="">Select Category</option></select></div>'
        res += '</form></td>'
        res += '</tr>'
        this.addContainer.html(res)
        this.addbuttonContainer.html('')
        setTimeout(()=>{
            this.subcategoriesOptions()
            this.categoriesOptions()
        })
    }

    subcategoriesOptions() {
        var details = ProductManagement.send_xml_request('GET', this.subcategories_api)[0]
        var res = '<option value="">Select Sub Category</option>'
        for (let index=0; index < details.length; index++) {
            res += '<option value="' + details[index] + '">' + details[index] + '</option>'
        }
        $('#sub_category').html(res).attr('onchange', '_p.categoriesOptions(this)')
    }

    categoriesOptions(that) {
        let api = this.categories_api
        api += that != undefined && that.value != "" ? ('?subcategory=' + that.value) : ''
        var details = ProductManagement.send_xml_request('GET', api)[0]
        var res = '<option value="">Select Category</option>'
        for (let index=0; index < details.length; index++) {
            res += '<option value="' + details[index] + '">' + details[index] + '</option>'
        }
        $('#category').html(res)
    }

    addProduct() {
        var data = {
            'product':  $('#product').val(),
            'subcategory': $('#sub_category').val(),
            'category': $('#category').val()
        }
        this.updateProducts(ProductManagement.send_xml_request("POST", this.product_api, JSON.stringify(data))[0])
        return false
    }

    cancel() {
        this.addbuttonContainer.html('<button class="btn btn-default" onclick="_p.addProductForm()">ADD</button>')
        this.addContainer.html('')
    }

    static getRowTemplate(row) {
        var res = '<tr class="item">'
        res += '<td><input type="checkbox" name="' + row.name + '"></td>'
        res += '<td>' + row.name + '</td>'
        res += '<td>' + row.category + '</td>'
        res += '<td>' + row.sub_category + '</td>'
        res += '</tr>'
        return res
    }

    static send_xml_request(method, api, data={}, sync=false, callback=null) {
        try {
            var xmlHttp = new XMLHttpRequest();
            xmlHttp.open( method, api, sync );
            if (callback != null && sync === true) {
                xmlHttp.onreadystatechange = function() {
                    if (this.readyState == 4 && this.status == 200) {
                        callback()
                    }
                };
            }
            xmlHttp.setRequestHeader('Accept', 'application/json')
            xmlHttp.setRequestHeader('Content-Type', 'application/json')
            xmlHttp.send( data );
            return [JSON.parse(xmlHttp.responseText), xmlHttp.status]
        } catch(e) {
            console.log(e)
        }
    }
}