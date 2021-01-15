(function (e) {
    function t(t) {
        for (var r, i, o = t[0], l = t[1], c = t[2], p = 0, d = []; p < o.length; p++) i = o[p], Object.prototype.hasOwnProperty.call(a, i) && a[i] && d.push(a[i][0]), a[i] = 0;
        for (r in l) Object.prototype.hasOwnProperty.call(l, r) && (e[r] = l[r]);
        u && u(t);
        while (d.length) d.shift()();
        return s.push.apply(s, c || []), n()
    }

    function n() {
        for (var e, t = 0; t < s.length; t++) {
            for (var n = s[t], r = !0, o = 1; o < n.length; o++) {
                var l = n[o];
                0 !== a[l] && (r = !1)
            }
            r && (s.splice(t--, 1), e = i(i.s = n[0]))
        }
        return e
    }

    var r = {}, a = {app: 0}, s = [];

    function i(t) {
        if (r[t]) return r[t].exports;
        var n = r[t] = {i: t, l: !1, exports: {}};
        return e[t].call(n.exports, n, n.exports, i), n.l = !0, n.exports
    }

    i.m = e, i.c = r, i.d = function (e, t, n) {
        i.o(e, t) || Object.defineProperty(e, t, {enumerable: !0, get: n})
    }, i.r = function (e) {
        "undefined" !== typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {value: "Module"}), Object.defineProperty(e, "__esModule", {value: !0})
    }, i.t = function (e, t) {
        if (1 & t && (e = i(e)), 8 & t) return e;
        if (4 & t && "object" === typeof e && e && e.__esModule) return e;
        var n = Object.create(null);
        if (i.r(n), Object.defineProperty(n, "default", {
            enumerable: !0,
            value: e
        }), 2 & t && "string" != typeof e) for (var r in e) i.d(n, r, function (t) {
            return e[t]
        }.bind(null, r));
        return n
    }, i.n = function (e) {
        var t = e && e.__esModule ? function () {
            return e["default"]
        } : function () {
            return e
        };
        return i.d(t, "a", t), t
    }, i.o = function (e, t) {
        return Object.prototype.hasOwnProperty.call(e, t)
    }, i.p = "/";
    var o = window["webpackJsonp"] = window["webpackJsonp"] || [], l = o.push.bind(o);
    o.push = t, o = o.slice();
    for (var c = 0; c < o.length; c++) t(o[c]);
    var u = l;
    s.push([0, "chunk-vendors"]), n()
})({
    0: function (e, t, n) {
        e.exports = n("56d7")
    }, "08cb": function (e, t, n) {
        e.exports = n.p + "img/partner.00fdaf0d.png"
    }, "0ecc": function (e, t, n) {
        "use strict";
        var r = n("3a9f"), a = n.n(r);
        a.a
    }, "18f8": function (e, t, n) {
    }, "1a8d": function (e, t, n) {
    }, "1fb4": function (e, t, n) {
        "use strict";
        var r = n("1a8d"), a = n.n(r);
        a.a
    }, "21da": function (e, t, n) {
        "use strict";
        var r = n("e8f0"), a = n.n(r);
        a.a
    }, "330a": function (e, t, n) {
        e.exports = n.p + "img/main-title.d8b37181.png"
    }, "3a9f": function (e, t, n) {
    }, "3d66": function (e, t, n) {
        "use strict";
        var r = n("9e5a"), a = n.n(r);
        a.a
    }, "3e1f": function (e, t, n) {
    }, 4066: function (e, t, n) {
        "use strict";
        var r = n("3e1f"), a = n.n(r);
        a.a
    }, "56d7": function (e, t, n) {
        "use strict";
        n.r(t);
        n("cadf"), n("551c"), n("f751"), n("097d");
        var r, a = n("2b0e"), s = function () {
                var e = this, t = e.$createElement, n = e._self._c || t;
                return n("div", {attrs: {id: "app"}}, [n("div", {staticClass: "logo-bg"}), n("div", {staticClass: "nav"}, [n("Header")], 1), n("keep-alive", [n("router-view")], 1)], 1)
            }, i = [], o = function () {
                var e = this, t = e.$createElement, n = e._self._c || t;
                return n("div", {staticClass: "header-wrapper"}, [n("div", {staticClass: "header"}, [e._m(0), n("div", {staticClass: "nav-wrapper"}, [n("router-link", {
                    staticClass: "nav-item",
                    attrs: {to: "/home"}
                }, [n("span", [e._v("首页")])]), n("router-link", {
                    staticClass: "nav-item",
                    attrs: {to: "/introduce"}
                }, [n("span", [e._v("产品介绍")])]), n("router-link", {
                    staticClass: "nav-item",
                    attrs: {to: "/partner"}
                }, [n("span", [e._v("生态伙伴")])]), n("router-link", {
                    staticClass: "nav-item",
                    attrs: {to: "/about"}
                }, [n("span", [e._v("关于我们")])]), n("router-link", {
                    staticClass: "nav-item",
                    attrs: {to: "/contact"}
                }, [n("span", [e._v("联系我们")])])], 1)])])
            }, l = [function () {
                var e = this, t = e.$createElement, n = e._self._c || t;
                return n("div", {staticClass: "logo"}, [n("h3", [e._v("足购科技 "), n("span", [e._v("ZUGO TECH")])])])
            }], c = {}, u = c, p = (n("dd02"), n("2877")), d = Object(p["a"])(u, o, l, !1, null, "1f2b0438", null),
            f = d.exports, m = {components: {Header: f}}, h = m,
            v = (n("1fb4"), Object(p["a"])(h, s, i, !1, null, "a81d0e70", null)), g = v.exports, T = n("8c4f"),
            _ = function () {
                var e = this, t = e.$createElement, n = e._self._c || t;
                return n("div", {staticClass: "home"}, [e._m(0), n("div", {staticClass: "wrapper"}, [n("div", {staticClass: "shoes"}, [n("canvas", {
                    ref: "comCanvas",
                    staticStyle: {width: "100px", height: "100px"}
                })]), e._m(1), e._m(2), e._m(3)]), n("Footer", {attrs: {isFixed: e.isFixed}})], 1)
            }, S = [function () {
                var e = this, t = e.$createElement, n = e._self._c || t;
                return n("div", {staticClass: "triangle-box"}, [n("div", {staticClass: "triangle"}), n("div", {staticClass: "blue-bg"})])
            }, function () {
                var e = this, t = e.$createElement, r = e._self._c || t;
                return r("div", {staticClass: "main-title"}, [r("img", {attrs: {src: n("330a")}})])
            }, function () {
                var e = this, t = e.$createElement, r = e._self._c || t;
                return r("div", {staticClass: "sub-title"}, [r("img", {attrs: {src: n("6cb6")}})])
            }, function () {
                var e = this, t = e.$createElement, r = e._self._c || t;
                return r("div", {staticClass: "art-title"}, [r("img", {attrs: {src: n("61f8")}})])
            }], y = (n("7f7f"), function () {
                var e = this, t = e.$createElement, n = e._self._c || t;
                return n("div", {class: e.isFixed ? "footer isfixed" : "footer"}, [e._v("Copyright © 2019 足购科技（杭州）有限公司 杭州市余杭区恒生科技园16号楼1单元5楼 电话号码：0571-88581570 浙ICP备19029902号")])
            }), b = [], M = {props: {isFixed: Boolean}}, x = M,
            E = (n("ac75"), Object(p["a"])(x, y, b, !1, null, "ce1f4d92", null)), R = E.exports, A = n("5a89"),
            w = (n("55dd"), n("7618")), L = (n("96cf"), n("3b8d")),
            C = (n("456d"), n("14b9"), n("a481"), n("ac6a"), n("5df3"), n("d225")), F = n("b0b4"), I = n("bd86"),
            O = (n("63d9"), n("9c29"), n("af56"), n("15ac"), n("34ef"), n("b05c"), "glTF"), P = 12,
            N = {JSON: 1313821514, BIN: 5130562}, U = {
                KHR_BINARY_GLTF: "KHR_binary_glTF",
                KHR_DRACO_MESH_COMPRESSION: "KHR_draco_mesh_compression",
                KHR_LIGHTS_PUNCTUAL: "KHR_lights_punctual",
                KHR_MATERIALS_PBR_SPECULAR_GLOSSINESS: "KHR_materials_pbrSpecularGlossiness",
                KHR_MATERIALS_UNLIT: "KHR_materials_unlit",
                KHR_TEXTURE_TRANSFORM: "KHR_texture_transform",
                MSFT_TEXTURE_DDS: "MSFT_texture_dds"
            }, H = {
                FLOAT: 5126,
                FLOAT_MAT3: 35675,
                FLOAT_MAT4: 35676,
                FLOAT_VEC2: 35664,
                FLOAT_VEC3: 35665,
                FLOAT_VEC4: 35666,
                LINEAR: 9729,
                REPEAT: 10497,
                SAMPLER_2D: 35678,
                POINTS: 0,
                LINES: 1,
                LINE_LOOP: 2,
                LINE_STRIP: 3,
                TRIANGLES: 4,
                TRIANGLE_STRIP: 5,
                TRIANGLE_FAN: 6,
                UNSIGNED_BYTE: 5121,
                UNSIGNED_SHORT: 5123
            }, D = {
                5120: Int8Array,
                5121: Uint8Array,
                5122: Int16Array,
                5123: Uint16Array,
                5125: Uint32Array,
                5126: Float32Array
            }, G = {9728: A["I"], 9729: A["w"], 9984: A["K"], 9985: A["y"], 9986: A["J"], 9987: A["x"]},
            k = {33071: A["f"], 33648: A["H"], 10497: A["W"]},
            j = {SCALAR: 1, VEC2: 2, VEC3: 3, VEC4: 4, MAT2: 4, MAT3: 9, MAT4: 16}, B = {
                POSITION: "position",
                NORMAL: "normal",
                TANGENT: "tangent",
                TEXCOORD_0: "uv",
                TEXCOORD_1: "uv2",
                COLOR_0: "color",
                WEIGHTS_0: "skinWeight",
                JOINTS_0: "skinIndex"
            }, K = {scale: "scale", translation: "position", rotation: "quaternion", weights: "morphTargetInfluences"},
            V = {CUBICSPLINE: void 0, LINEAR: A["r"], STEP: A["q"]},
            X = {OPAQUE: "OPAQUE", MASK: "MASK", BLEND: "BLEND"}, $ = {"image/png": A["U"], "image/jpeg": A["V"]},
            z = function () {
                function e(t) {
                    Object(C["a"])(this, e), Object(I["a"])(this, "crossOrigin", "anonymous"), this.manager = void 0 !== t ? t : A["h"], this.dracoLoader = null, this.ddsLoader = null
                }

                return Object(F["a"])(e, [{
                    key: "setCrossOrigin", value: function (e) {
                        return this.crossOrigin = e, this
                    }
                }, {
                    key: "setPath", value: function (e) {
                        return this.path = e, this
                    }
                }, {
                    key: "setResourcePath", value: function (e) {
                        return this.resourcePath = e, this
                    }
                }, {
                    key: "setDRACOLoader", value: function (e) {
                        return this.dracoLoader = e, this
                    }
                }, {
                    key: "setDDSLoader", value: function (e) {
                        return this.ddsLoader = e, this
                    }
                }, {
                    key: "load", value: function (e, t, n, r) {
                        var a, s = this;
                        a = void 0 !== this.resourcePath ? this.resourcePath : void 0 !== this.path ? this.path : A["A"].extractUrlBase(e), s.manager.itemStart(e);
                        var i = function (t) {
                            r ? r(t) : console.error(t), s.manager.itemError(e), s.manager.itemEnd(e)
                        }, o = new A["k"](s.manager);
                        o.setPath(this.path), o.setResponseType("arraybuffer"), "use-credentials" === s.crossOrigin && o.setWithCredentials(!0), o.load(e, function (n) {
                            try {
                                s.parse(n, a, function (n) {
                                    t(n), s.manager.itemEnd(e)
                                }, i)
                            } catch (r) {
                                i(r)
                            }
                        }, n, i)
                    }
                }, {
                    key: "parse", value: function (e, t, n, r) {
                        var a, s = {};
                        if ("string" === typeof e) a = e; else {
                            var i = A["A"].decodeText(new Uint8Array(e, 0, 4));
                            if (i === O) {
                                try {
                                    s[U.KHR_BINARY_GLTF] = new Y(e)
                                } catch (d) {
                                    return void (r && r(d))
                                }
                                a = s[U.KHR_BINARY_GLTF].content
                            } else a = A["A"].decodeText(new Uint8Array(e))
                        }
                        var o = JSON.parse(a);
                        if (void 0 === o.asset || o.asset.version[0] < 2) r && r(new Error("THREE.GLTFLoader: Unsupported asset. glTF versions >=2.0 are supported. Use LegacyGLTFLoader instead.")); else {
                            if (o.extensionsUsed) for (var l = 0; l < o.extensionsUsed.length; ++l) {
                                var c = o.extensionsUsed[l], u = o.extensionsRequired || [];
                                switch (c) {
                                    case U.KHR_LIGHTS_PUNCTUAL:
                                        s[c] = new W(o);
                                        break;
                                    case U.KHR_MATERIALS_UNLIT:
                                        s[c] = new Z;
                                        break;
                                    case U.KHR_MATERIALS_PBR_SPECULAR_GLOSSINESS:
                                        s[c] = new J;
                                        break;
                                    case U.KHR_DRACO_MESH_COMPRESSION:
                                        s[c] = new q(o, this.dracoLoader);
                                        break;
                                    case U.MSFT_TEXTURE_DDS:
                                        s[U.MSFT_TEXTURE_DDS] = new Q(this.ddsLoader);
                                        break;
                                    case U.KHR_TEXTURE_TRANSFORM:
                                        s[U.KHR_TEXTURE_TRANSFORM] = new ee;
                                        break;
                                    default:
                                        u.indexOf(c) >= 0 && console.warn('THREE.GLTFLoader: Unknown extension "' + c + '".')
                                }
                            }
                            var p = new te(o, s, {
                                path: t || this.resourcePath || "",
                                crossOrigin: this.crossOrigin,
                                manager: this.manager
                            });
                            p.parse(n, r)
                        }
                    }
                }]), e
            }();

        function Y(e) {
            this.name = U.KHR_BINARY_GLTF, this.content = null, this.body = null;
            var t = new DataView(e, 0, P);
            if (this.header = {
                magic: A["A"].decodeText(new Uint8Array(e.slice(0, 4))),
                version: t.getUint32(4, !0),
                length: t.getUint32(8, !0)
            }, this.header.magic !== O) throw new Error("THREE.GLTFLoader: Unsupported glTF-Binary header.");
            if (this.header.version < 2) throw new Error("THREE.GLTFLoader: Legacy binary file detected. Use LegacyGLTFLoader instead.");
            var n = new DataView(e, P), r = 0;
            while (r < n.byteLength) {
                var a = n.getUint32(r, !0);
                r += 4;
                var s = n.getUint32(r, !0);
                if (r += 4, s === N.JSON) {
                    var i = new Uint8Array(e, P + r, a);
                    this.content = A["A"].decodeText(i)
                } else if (s === N.BIN) {
                    var o = P + r;
                    this.body = e.slice(o, o + a)
                }
                r += a
            }
            if (null === this.content) throw new Error("THREE.GLTFLoader: JSON content not found.")
        }

        function W(e) {
            this.name = U.KHR_LIGHTS_PUNCTUAL;
            var t = e.extensions && e.extensions[U.KHR_LIGHTS_PUNCTUAL] || {};
            this.lightDefs = t.lights || []
        }

        function Z() {
            this.name = U.KHR_MATERIALS_UNLIT
        }

        function J() {
            return {
                name: U.KHR_MATERIALS_PBR_SPECULAR_GLOSSINESS,
                specularGlossinessParams: ["color", "map", "lightMap", "lightMapIntensity", "aoMap", "aoMapIntensity", "emissive", "emissiveIntensity", "emissiveMap", "bumpMap", "bumpScale", "normalMap", "displacementMap", "displacementScale", "displacementBias", "specularMap", "specular", "glossinessMap", "glossiness", "alphaMap", "envMap", "envMapIntensity", "refractionRatio"],
                getMaterialType: function () {
                    return A["Z"]
                },
                extendParams: function (e, t, n) {
                    var r = t.extensions[this.name], a = A["Y"]["standard"], s = A["gb"].clone(a.uniforms),
                        i = ["#ifdef USE_SPECULARMAP", "\tuniform sampler2D specularMap;", "#endif"].join("\n"),
                        o = ["#ifdef USE_GLOSSINESSMAP", "\tuniform sampler2D glossinessMap;", "#endif"].join("\n"),
                        l = ["vec3 specularFactor = specular;", "#ifdef USE_SPECULARMAP", "\tvec4 texelSpecular = texture2D( specularMap, vUv );", "\ttexelSpecular = sRGBToLinear( texelSpecular );", "\t// reads channel RGB, compatible with a glTF Specular-Glossiness (RGBA) texture", "\tspecularFactor *= texelSpecular.rgb;", "#endif"].join("\n"),
                        c = ["float glossinessFactor = glossiness;", "#ifdef USE_GLOSSINESSMAP", "\tvec4 texelGlossiness = texture2D( glossinessMap, vUv );", "\t// reads channel A, compatible with a glTF Specular-Glossiness (RGBA) texture", "\tglossinessFactor *= texelGlossiness.a;", "#endif"].join("\n"),
                        u = ["PhysicalMaterial material;", "material.diffuseColor = diffuseColor.rgb;", "material.specularRoughness = clamp( 1.0 - glossinessFactor, 0.04, 1.0 );", "material.specularColor = specularFactor.rgb;"].join("\n"),
                        p = a.fragmentShader.replace("uniform float roughness;", "uniform vec3 specular;").replace("uniform float metalness;", "uniform float glossiness;").replace("#include <roughnessmap_pars_fragment>", i).replace("#include <metalnessmap_pars_fragment>", o).replace("#include <roughnessmap_fragment>", l).replace("#include <metalnessmap_fragment>", c).replace("#include <lights_physical_fragment>", u);
                    delete s.roughness, delete s.metalness, delete s.roughnessMap, delete s.metalnessMap, s.specular = {value: (new A["g"]).setHex(1118481)}, s.glossiness = {value: .5}, s.specularMap = {value: null}, s.glossinessMap = {value: null}, e.vertexShader = a.vertexShader, e.fragmentShader = p, e.uniforms = s, e.defines = {STANDARD: ""}, e.color = new A["g"](1, 1, 1), e.opacity = 1;
                    var d = [];
                    if (Array.isArray(r.diffuseFactor)) {
                        var f = r.diffuseFactor;
                        e.color.fromArray(f), e.opacity = f[3]
                    }
                    if (void 0 !== r.diffuseTexture && d.push(n.assignTexture(e, "map", r.diffuseTexture)), e.emissive = new A["g"](0, 0, 0), e.glossiness = void 0 !== r.glossinessFactor ? r.glossinessFactor : 1, e.specular = new A["g"](1, 1, 1), Array.isArray(r.specularFactor) && e.specular.fromArray(r.specularFactor), void 0 !== r.specularGlossinessTexture) {
                        var m = r.specularGlossinessTexture;
                        d.push(n.assignTexture(e, "glossinessMap", m)), d.push(n.assignTexture(e, "specularMap", m))
                    }
                    return Promise.all(d)
                },
                createMaterial: function (e) {
                    var t = new A["Z"]({
                        defines: e.defines,
                        vertexShader: e.vertexShader,
                        fragmentShader: e.fragmentShader,
                        uniforms: e.uniforms,
                        fog: !0,
                        lights: !0,
                        opacity: e.opacity,
                        transparent: e.transparent
                    });
                    return t.isGLTFSpecularGlossinessMaterial = !0, t.color = e.color, t.map = void 0 === e.map ? null : e.map, t.lightMap = null, t.lightMapIntensity = 1, t.aoMap = void 0 === e.aoMap ? null : e.aoMap, t.aoMapIntensity = 1, t.emissive = e.emissive, t.emissiveIntensity = 1, t.emissiveMap = void 0 === e.emissiveMap ? null : e.emissiveMap, t.bumpMap = void 0 === e.bumpMap ? null : e.bumpMap, t.bumpScale = 1, t.normalMap = void 0 === e.normalMap ? null : e.normalMap, e.normalScale && (t.normalScale = e.normalScale), t.displacementMap = null, t.displacementScale = 1, t.displacementBias = 0, t.specularMap = void 0 === e.specularMap ? null : e.specularMap, t.specular = e.specular, t.glossinessMap = void 0 === e.glossinessMap ? null : e.glossinessMap, t.glossiness = e.glossiness, t.alphaMap = null, t.envMap = void 0 === e.envMap ? null : e.envMap, t.envMapIntensity = 1, t.refractionRatio = .98, t.extensions.derivatives = !0, t
                },
                cloneMaterial: function (e) {
                    var t = e.clone();
                    t.isGLTFSpecularGlossinessMaterial = !0;
                    for (var n = this.specularGlossinessParams, r = 0, a = n.length; r < a; r++) {
                        var s = e[n[r]];
                        t[n[r]] = s && s.isColor ? s.clone() : s
                    }
                    return t
                },
                refreshUniforms: function (e, t, n, r, a) {
                    if (!0 === a.isGLTFSpecularGlossinessMaterial) {
                        var s, i = a.uniforms, o = a.defines;
                        i.opacity.value = a.opacity, i.diffuse.value.copy(a.color), i.emissive.value.copy(a.emissive).multiplyScalar(a.emissiveIntensity), i.map.value = a.map, i.specularMap.value = a.specularMap, i.alphaMap.value = a.alphaMap, i.lightMap.value = a.lightMap, i.lightMapIntensity.value = a.lightMapIntensity, i.aoMap.value = a.aoMap, i.aoMapIntensity.value = a.aoMapIntensity, a.map ? s = a.map : a.specularMap ? s = a.specularMap : a.displacementMap ? s = a.displacementMap : a.normalMap ? s = a.normalMap : a.bumpMap ? s = a.bumpMap : a.glossinessMap ? s = a.glossinessMap : a.alphaMap ? s = a.alphaMap : a.emissiveMap && (s = a.emissiveMap), void 0 !== s && (s.isWebGLRenderTarget && (s = s.texture), !0 === s.matrixAutoUpdate && s.updateMatrix(), i.uvTransform.value.copy(s.matrix)), a.envMap && (i.envMap.value = a.envMap, i.envMapIntensity.value = a.envMapIntensity, i.flipEnvMap.value = a.envMap.isCubeTexture ? -1 : 1, i.reflectivity.value = a.reflectivity, i.refractionRatio.value = a.refractionRatio, i.maxMipLevel.value = e.properties.get(a.envMap).__maxMipLevel), i.specular.value.copy(a.specular), i.glossiness.value = a.glossiness, i.glossinessMap.value = a.glossinessMap, i.emissiveMap.value = a.emissiveMap, i.bumpMap.value = a.bumpMap, i.normalMap.value = a.normalMap, i.displacementMap.value = a.displacementMap, i.displacementScale.value = a.displacementScale, i.displacementBias.value = a.displacementBias, null !== i.glossinessMap.value && void 0 === o.USE_GLOSSINESSMAP && (o.USE_GLOSSINESSMAP = "", o.USE_ROUGHNESSMAP = ""), null === i.glossinessMap.value && void 0 !== o.USE_GLOSSINESSMAP && (delete o.USE_GLOSSINESSMAP, delete o.USE_ROUGHNESSMAP)
                    }
                }
            }
        }

        function q(e, t) {
            if (!t) throw new Error("THREE.GLTFLoader: No DRACOLoader instance provided.");
            this.name = U.KHR_DRACO_MESH_COMPRESSION, this.json = e, this.dracoLoader = t
        }

        function Q(e) {
            if (!e) throw new Error("THREE.GLTFLoader: Attempting to load .dds texture without importing THREE.DDSLoader");
            this.name = U.MSFT_TEXTURE_DDS, this.ddsLoader = e
        }

        function ee() {
            this.name = U.KHR_TEXTURE_TRANSFORM
        }

        function te(e, t, n) {
            this.json = e || {}, this.extensions = t || {}, this.options = n || {}, this.cache = new re, this.primitiveCache = {}, this.textureLoader = new A["db"](this.options.manager), this.textureLoader.setCrossOrigin(this.options.crossOrigin), this.fileLoader = new A["k"](this.options.manager), this.fileLoader.setResponseType("arraybuffer"), "use-credentials" === this.options.crossOrigin && this.fileLoader.setWithCredentials(!0)
        }

        function ne(e, t) {
            void 0 !== t.extras && ("object" === Object(w["a"])(t.extras) ? Object.assign(e.userData, t.extras) : console.warn("THREE.GLTFLoader: Ignoring primitive type .extras, " + t.extras))
        }

        function re() {
            var e = {};
            return {
                get: function (t) {
                    return e[t]
                }, add: function (t, n) {
                    e[t] = n
                }, remove: function (t) {
                    delete e[t]
                }, removeAll: function () {
                    e = {}
                }
            }
        }

        function ae(e, t, n) {
            for (var r in n.extensions) void 0 === e[r] && (t.userData.gltfExtensions = t.userData.gltfExtensions || {}, t.userData.gltfExtensions[r] = n.extensions[r])
        }

        function se(e, t) {
            return "string" !== typeof e || "" === e ? "" : (/^https?:\/\//i.test(t) && /^\//.test(e) && (t = t.replace(/(^https?:\/\/[^\/]+).*/i, "$1")), /^(https?:)?\/\//i.test(e) ? e : /^data:.*,.*$/i.test(e) ? e : /^blob:.*$/i.test(e) ? e : t + e)
        }

        function ie(e, t, n) {
            var r = t.attributes, a = [];

            function s(t, r) {
                return n.getDependency("accessor", t).then(function (t) {
                    e.addAttribute(r, t)
                })
            }

            for (var i in r) {
                var o = B[i] || i.toLowerCase();
                o in e.attributes || a.push(s(r[i], o))
            }
            if (void 0 !== t.indices && !e.index) {
                var l = n.getDependency("accessor", t.indices).then(function (t) {
                    e.setIndex(t)
                });
                a.push(l)
            }
            return ne(e, t), Promise.all(a).then(function () {
                return void 0 !== t.targets ? oe(e, t.targets, n) : e
            })
        }

        function oe(e, t, n) {
            for (var r = !1, a = !1, s = 0, i = t.length; s < i; s++) {
                var o = t[s];
                if (void 0 !== o.POSITION && (r = !0), void 0 !== o.NORMAL && (a = !0), r && a) break
            }
            if (!r && !a) return Promise.resolve(e);
            for (var l = [], c = [], u = 0, p = t.length; u < p; u++) {
                var d = t[u];
                if (r) {
                    var f = void 0 !== d.POSITION ? n.getDependency("accessor", d.POSITION) : e.attributes.position;
                    l.push(f)
                }
                if (a) {
                    var m = void 0 !== d.NORMAL ? n.getDependency("accessor", d.NORMAL) : e.attributes.normal;
                    c.push(m)
                }
            }
            return Promise.all([Promise.all(l), Promise.all(c)]).then(function (n) {
                for (var s = n[0], i = n[1], o = 0, l = s.length; o < l; o++) e.attributes.position !== s[o] && (s[o] = fe(s[o]));
                for (var c = 0, u = i.length; c < u; c++) e.attributes.normal !== i[c] && (i[c] = fe(i[c]));
                for (var p = 0, d = t.length; p < d; p++) {
                    var f = t[p], m = "morphTarget" + p;
                    if (r && void 0 !== f.POSITION) {
                        var h = s[p];
                        h.name = m;
                        for (var v = e.attributes.position, g = 0, T = h.count; g < T; g++) h.setXYZ(g, h.getX(g) + v.getX(g), h.getY(g) + v.getY(g), h.getZ(g) + v.getZ(g))
                    }
                    if (a && void 0 !== f.NORMAL) {
                        var _ = i[p];
                        _.name = m;
                        for (var S = e.attributes.normal, y = 0, b = _.count; y < b; y++) _.setXYZ(y, _.getX(y) + S.getX(y), _.getY(y) + S.getY(y), _.getZ(y) + S.getZ(y))
                    }
                }
                return r && (e.morphAttributes.position = s), a && (e.morphAttributes.normal = i), e
            })
        }

        function le(e) {
            var t, n = e.extensions && e.extensions[U.KHR_DRACO_MESH_COMPRESSION];
            return t = n ? "draco:".concat(n.bufferView, ":").concat(n.indices, ":").concat(ce(n.attributes)) : e.indices + ":" + ce(e.attributes) + ":" + e.mode, t
        }

        function ce(e) {
            for (var t = "", n = Object.keys(e).sort(), r = 0, a = n.length; r < a; r++) t += n[r] + ":" + e[n[r]] + ";";
            return t
        }

        function ue() {
            return r = r || new A["G"]({
                color: 16777215,
                emissive: 0,
                metalness: 1,
                roughness: 1,
                transparent: !1,
                depthTest: !0,
                side: A["l"]
            }), r
        }

        function pe(e, t) {
            if (e.updateMorphTargets(), void 0 !== t.weights) for (var n = 0, r = t.weights.length; n < r; n++) e.morphTargetInfluences[n] = t.weights[n];
            if (t.extras && Array.isArray(t.extras.targetNames)) {
                var a = t.extras.targetNames;
                if (e.morphTargetInfluences.length === a.length) {
                    e.morphTargetDictionary = {};
                    for (var s = 0, i = a.length; s < i; s++) e.morphTargetDictionary[a[s]] = s
                } else console.warn("THREE.GLTFLoader: Invalid extras.targetNames length. Ignoring names.")
            }
        }

        function de(e, t, n, r) {
            A["p"].call(this, e, t, n, r)
        }

        function fe(e) {
            if (e.isInterleavedBufferAttribute) {
                for (var t = e.count, n = e.itemSize, r = e.array.slice(0, t * n), a = 0, s = 0; a < t; ++a) r[s++] = e.getX(a), n >= 2 && (r[s++] = e.getY(a)), n >= 3 && (r[s++] = e.getZ(a)), n >= 4 && (r[s++] = e.getW(a));
                return new A["d"](r, n, e.normalized)
            }
            return e.clone()
        }

        W.prototype.loadLight = function (e) {
            var t, n = this.lightDefs[e], r = new A["g"](16777215);
            void 0 !== n.color && r.fromArray(n.color);
            var a = void 0 !== n.range ? n.range : 0;
            switch (n.type) {
                case"directional":
                    t = new A["i"](r), t.target.position.set(0, 0, -1), t.add(t.target);
                    break;
                case"point":
                    t = new A["P"](r), t.distance = a;
                    break;
                case"spot":
                    t = new A["cb"](r), t.distance = a, n.spot = n.spot || {}, n.spot.innerConeAngle = void 0 !== n.spot.innerConeAngle ? n.spot.innerConeAngle : 0, n.spot.outerConeAngle = void 0 !== n.spot.outerConeAngle ? n.spot.outerConeAngle : Math.PI / 4, t.angle = n.spot.outerConeAngle, t.penumbra = 1 - n.spot.innerConeAngle / n.spot.outerConeAngle, t.target.position.set(0, 0, -1), t.add(t.target);
                    break;
                default:
                    throw new Error('THREE.GLTFLoader: Unexpected light type, "' + n.type + '".')
            }
            return t.position.set(0, 0, 0), t.decay = 2, void 0 !== n.intensity && (t.intensity = n.intensity), t.name = n.name || "light_" + e, Promise.resolve(t)
        }, Z.prototype.getMaterialType = function () {
            return A["F"]
        }, Z.prototype.extendParams = function (e, t, n) {
            var r = [];
            e.color = new A["g"](1, 1, 1), e.opacity = 1;
            var a = t.pbrMetallicRoughness;
            if (a) {
                if (Array.isArray(a.baseColorFactor)) {
                    var s = a.baseColorFactor;
                    e.color.fromArray(s), e.opacity = s[3]
                }
                void 0 !== a.baseColorTexture && r.push(n.assignTexture(e, "map", a.baseColorTexture))
            }
            return Promise.all(r)
        }, q.prototype.decodePrimitive = function (e, t) {
            var n, r = this.json, a = this.dracoLoader, s = e.extensions[this.name].bufferView,
                i = e.extensions[this.name].attributes, o = {}, l = {}, c = {};
            for (var u in i) n = B[u] || u.toLowerCase(), o[n] = i[u];
            for (u in e.attributes) if (n = B[u] || u.toLowerCase(), void 0 !== i[u]) {
                var p = r.accessors[e.attributes[u]], d = D[p.componentType];
                c[n] = d, l[n] = !0 === p.normalized
            }
            return t.getDependency("bufferView", s).then(function (e) {
                return new Promise(function (t) {
                    a.decodeDracoFile(e, function (e) {
                        for (var n in e.attributes) {
                            var r = e.attributes[n], a = l[n];
                            void 0 !== a && (r.normalized = a)
                        }
                        t(e)
                    }, o, c)
                })
            })
        }, ee.prototype.extendTexture = function (e, t) {
            return e = e.clone(), void 0 !== t.offset && e.offset.fromArray(t.offset), void 0 !== t.rotation && (e.rotation = t.rotation), void 0 !== t.scale && e.repeat.fromArray(t.scale), void 0 !== t.texCoord && console.warn('THREE.GLTFLoader: Custom UV sets in "' + this.name + '" extension not yet supported.'), e.needsUpdate = !0, e
        }, te.prototype.parse = function (e, t) {
            var n = this, r = this.json, a = this.extensions;
            this.cache.removeAll(), this.markDefs(), Promise.all([this.getDependencies("scene"), this.getDependencies("animation"), this.getDependencies("camera")]).then(function (t) {
                var s = {
                    scene: t[0][r.scene || 0],
                    scenes: t[0],
                    animations: t[1],
                    cameras: t[2],
                    asset: r.asset,
                    parser: n,
                    userData: {}
                };
                ae(a, s, r), ne(s, r), e(s)
            }).catch(t)
        }, te.prototype.markDefs = function () {
            for (var e = this.json.nodes || [], t = this.json.skins || [], n = this.json.meshes || [], r = {}, a = {}, s = 0, i = t.length; s < i; s++) for (var o = t[s].joints, l = 0, c = o.length; l < c; l++) e[o[l]].isBone = !0;
            for (var u = 0, p = e.length; u < p; u++) {
                var d = e[u];
                void 0 !== d.mesh && (void 0 === r[d.mesh] && (r[d.mesh] = a[d.mesh] = 0), r[d.mesh]++, void 0 !== d.skin && (n[d.mesh].isSkinnedMesh = !0))
            }
            this.json.meshReferences = r, this.json.meshUses = a
        }, te.prototype.getDependency = function (e, t) {
            var n = e + ":" + t, r = this.cache.get(n);
            if (!r) {
                switch (e) {
                    case"scene":
                        r = this.loadScene(t);
                        break;
                    case"node":
                        r = this.loadNode(t);
                        break;
                    case"mesh":
                        r = this.loadMesh(t);
                        break;
                    case"accessor":
                        r = this.loadAccessor(t);
                        break;
                    case"bufferView":
                        r = this.loadBufferView(t);
                        break;
                    case"buffer":
                        r = this.loadBuffer(t);
                        break;
                    case"material":
                        r = this.loadMaterial(t);
                        break;
                    case"texture":
                        r = this.loadTexture(t);
                        break;
                    case"skin":
                        r = this.loadSkin(t);
                        break;
                    case"animation":
                        r = this.loadAnimation(t);
                        break;
                    case"camera":
                        r = this.loadCamera(t);
                        break;
                    case"light":
                        r = this.extensions[U.KHR_LIGHTS_PUNCTUAL].loadLight(t);
                        break;
                    default:
                        throw new Error("Unknown type: " + e)
                }
                this.cache.add(n, r)
            }
            return r
        }, te.prototype.getDependencies = function (e) {
            var t = this.cache.get(e);
            if (!t) {
                var n = this, r = this.json[e + ("mesh" === e ? "es" : "s")] || [];
                t = Promise.all(r.map(function (t, r) {
                    return n.getDependency(e, r)
                })), this.cache.add(e, t)
            }
            return t
        }, te.prototype.loadBuffer = function (e) {
            var t = this.json.buffers[e], n = this.fileLoader;
            if (t.type && "arraybuffer" !== t.type) throw new Error("THREE.GLTFLoader: " + t.type + " buffer type is not supported.");
            if (void 0 === t.uri && 0 === e) return Promise.resolve(this.extensions[U.KHR_BINARY_GLTF].body);
            var r = this.options;
            return new Promise(function (e, a) {
                n.load(se(t.uri, r.path), e, void 0, function () {
                    a(new Error('THREE.GLTFLoader: Failed to load buffer "' + t.uri + '".'))
                })
            })
        }, te.prototype.loadBufferView = function (e) {
            var t = this.json.bufferViews[e];
            return this.getDependency("buffer", t.buffer).then(function (e) {
                var n = t.byteLength || 0, r = t.byteOffset || 0;
                return e.slice(r, r + n)
            })
        }, te.prototype.loadAccessor = function (e) {
            var t = this, n = this.json, r = this.json.accessors[e];
            if (void 0 === r.bufferView && void 0 === r.sparse) return Promise.resolve(null);
            var a = [];
            return void 0 !== r.bufferView ? a.push(this.getDependency("bufferView", r.bufferView)) : a.push(null), void 0 !== r.sparse && (a.push(this.getDependency("bufferView", r.sparse.indices.bufferView)), a.push(this.getDependency("bufferView", r.sparse.values.bufferView))), Promise.all(a).then(function (e) {
                var a, s, i = e[0], o = j[r.type], l = D[r.componentType], c = l.BYTES_PER_ELEMENT, u = c * o,
                    p = r.byteOffset || 0,
                    d = void 0 !== r.bufferView ? n.bufferViews[r.bufferView].byteStride : void 0,
                    f = !0 === r.normalized;
                if (d && d !== u) {
                    var m = Math.floor(p / d),
                        h = "InterleavedBuffer:" + r.bufferView + ":" + r.componentType + ":" + m + ":" + r.count,
                        v = t.cache.get(h);
                    v || (a = new l(i, m * d, r.count * d / c), v = new A["n"](a, d / c), t.cache.add(h, v)), s = new A["o"](v, o, p % d / c, f)
                } else a = null === i ? new l(r.count * o) : new l(i, p, r.count * o), s = new A["d"](a, o, f);
                if (void 0 !== r.sparse) {
                    var g = j.SCALAR, T = D[r.sparse.indices.componentType], _ = r.sparse.indices.byteOffset || 0,
                        S = r.sparse.values.byteOffset || 0, y = new T(e[1], _, r.sparse.count * g),
                        b = new l(e[2], S, r.sparse.count * o);
                    null !== i && s.setArray(s.array.slice());
                    for (var M = 0, x = y.length; M < x; M++) {
                        var E = y[M];
                        if (s.setX(E, b[M * o]), o >= 2 && s.setY(E, b[M * o + 1]), o >= 3 && s.setZ(E, b[M * o + 2]), o >= 4 && s.setW(E, b[M * o + 3]), o >= 5) throw new Error("THREE.GLTFLoader: Unsupported itemSize in sparse BufferAttribute.")
                    }
                }
                return s
            })
        }, te.prototype.loadTexture = function (e) {
            var t, n = this, r = this.json, a = this.options, s = this.textureLoader,
                i = window.URL || window.webkitURL, o = r.textures[e], l = o.extensions || {};
            t = l[U.MSFT_TEXTURE_DDS] ? r.images[l[U.MSFT_TEXTURE_DDS].source] : r.images[o.source];
            var c = t.uri, u = !1;
            return void 0 !== t.bufferView && (c = n.getDependency("bufferView", t.bufferView).then(function (e) {
                u = !0;
                var n = new Blob([e], {type: t.mimeType});
                return c = i.createObjectURL(n), c
            })), Promise.resolve(c).then(function (e) {
                var t = A["z"].Handlers.get(e);
                return t || (t = l[U.MSFT_TEXTURE_DDS] ? n.extensions[U.MSFT_TEXTURE_DDS].ddsLoader : s), new Promise(function (n, r) {
                    t.load(se(e, a.path), n, void 0, r)
                })
            }).then(function (e) {
                !0 === u && i.revokeObjectURL(c), e.flipY = !1, void 0 !== o.name && (e.name = o.name), t.mimeType in $ && (e.format = $[t.mimeType]);
                var n = r.samplers || {}, a = n[o.sampler] || {};
                return e.magFilter = G[a.magFilter] || A["w"], e.minFilter = G[a.minFilter] || A["x"], e.wrapS = k[a.wrapS] || A["W"], e.wrapT = k[a.wrapT] || A["W"], e
            })
        }, te.prototype.assignTexture = function (e, t, n) {
            var r = this;
            return this.getDependency("texture", n.index).then(function (a) {
                if (!a.isCompressedTexture) switch (t) {
                    case"aoMap":
                    case"emissiveMap":
                    case"metalnessMap":
                    case"normalMap":
                    case"roughnessMap":
                        a.format = A["V"];
                        break
                }
                if (r.extensions[U.KHR_TEXTURE_TRANSFORM]) {
                    var s = void 0 !== n.extensions ? n.extensions[U.KHR_TEXTURE_TRANSFORM] : void 0;
                    s && (a = r.extensions[U.KHR_TEXTURE_TRANSFORM].extendTexture(a, s))
                }
                e[t] = a
            })
        }, te.prototype.assignFinalMaterial = function (e) {
            var t = e.geometry, n = e.material, r = this.extensions, a = void 0 !== t.attributes.tangent,
                s = void 0 !== t.attributes.color, i = void 0 === t.attributes.normal, o = !0 === e.isSkinnedMesh,
                l = Object.keys(t.morphAttributes).length > 0, c = l && void 0 !== t.morphAttributes.normal;
            if (e.isPoints) {
                var u = "PointsMaterial:" + n.uuid, p = this.cache.get(u);
                p || (p = new A["R"], A["B"].prototype.copy.call(p, n), p.color.copy(n.color), p.map = n.map, p.lights = !1, this.cache.add(u, p)), n = p
            } else if (e.isLine) {
                var d = "LineBasicMaterial:" + n.uuid, f = this.cache.get(d);
                f || (f = new A["t"], A["B"].prototype.copy.call(f, n), f.color.copy(n.color), f.lights = !1, this.cache.add(d, f)), n = f
            }
            if (a || s || i || o || l) {
                var m = "ClonedMaterial:" + n.uuid + ":";
                n.isGLTFSpecularGlossinessMaterial && (m += "specular-glossiness:"), o && (m += "skinning:"), a && (m += "vertex-tangents:"), s && (m += "vertex-colors:"), i && (m += "flat-shading:"), l && (m += "morph-targets:"), c && (m += "morph-normals:");
                var h = this.cache.get(m);
                h || (h = n.isGLTFSpecularGlossinessMaterial ? r[U.KHR_MATERIALS_PBR_SPECULAR_GLOSSINESS].cloneMaterial(n) : n.clone(), o && (h.skinning = !0), a && (h.vertexTangents = !0), s && (h.vertexColors = A["jb"]), i && (h.flatShading = !0), l && (h.morphTargets = !0), c && (h.morphNormals = !0), this.cache.add(m, h)), n = h
            }
            n.aoMap && void 0 === t.attributes.uv2 && void 0 !== t.attributes.uv && (console.log("THREE.GLTFLoader: Duplicating UVs to support aoMap."), t.addAttribute("uv2", new A["d"](t.attributes.uv.array, 2))), n.isGLTFSpecularGlossinessMaterial && (e.onBeforeRender = r[U.KHR_MATERIALS_PBR_SPECULAR_GLOSSINESS].refreshUniforms), e.material = n
        }, te.prototype.loadMaterial = function (e) {
            var t, n = this, r = this.json, a = this.extensions, s = r.materials[e], i = {}, o = s.extensions || {},
                l = [];
            if (o[U.KHR_MATERIALS_PBR_SPECULAR_GLOSSINESS]) {
                var c = a[U.KHR_MATERIALS_PBR_SPECULAR_GLOSSINESS];
                t = c.getMaterialType(), l.push(c.extendParams(i, s, n))
            } else if (o[U.KHR_MATERIALS_UNLIT]) {
                var u = a[U.KHR_MATERIALS_UNLIT];
                t = u.getMaterialType(), l.push(u.extendParams(i, s, n))
            } else {
                t = A["G"];
                var p = s.pbrMetallicRoughness || {};
                if (i.color = new A["g"](1, 1, 1), i.opacity = 1, Array.isArray(p.baseColorFactor)) {
                    var d = p.baseColorFactor;
                    i.color.fromArray(d), i.opacity = d[3]
                }
                void 0 !== p.baseColorTexture && l.push(n.assignTexture(i, "map", p.baseColorTexture)), i.metalness = void 0 !== p.metallicFactor ? p.metallicFactor : 1, i.roughness = void 0 !== p.roughnessFactor ? p.roughnessFactor : 1, void 0 !== p.metallicRoughnessTexture && (l.push(n.assignTexture(i, "metalnessMap", p.metallicRoughnessTexture)), l.push(n.assignTexture(i, "roughnessMap", p.metallicRoughnessTexture)))
            }
            !0 === s.doubleSided && (i.side = A["j"]);
            var f = s.alphaMode || X.OPAQUE;
            return f === X.BLEND ? i.transparent = !0 : (i.transparent = !1, f === X.MASK && (i.alphaTest = void 0 !== s.alphaCutoff ? s.alphaCutoff : .5)), void 0 !== s.normalTexture && t !== A["F"] && (l.push(n.assignTexture(i, "normalMap", s.normalTexture)), i.normalScale = new A["hb"](1, 1), void 0 !== s.normalTexture.scale && i.normalScale.set(s.normalTexture.scale, s.normalTexture.scale)), void 0 !== s.occlusionTexture && t !== A["F"] && (l.push(n.assignTexture(i, "aoMap", s.occlusionTexture)), void 0 !== s.occlusionTexture.strength && (i.aoMapIntensity = s.occlusionTexture.strength)), void 0 !== s.emissiveFactor && t !== A["F"] && (i.emissive = (new A["g"]).fromArray(s.emissiveFactor)), void 0 !== s.emissiveTexture && t !== A["F"] && l.push(n.assignTexture(i, "emissiveMap", s.emissiveTexture)), Promise.all(l).then(function () {
                var e;
                return e = t === A["Z"] ? a[U.KHR_MATERIALS_PBR_SPECULAR_GLOSSINESS].createMaterial(i) : new t(i), void 0 !== s.name && (e.name = s.name), e.map && (e.map.encoding = A["lb"]), e.emissiveMap && (e.emissiveMap.encoding = A["lb"]), e.specularMap && (e.specularMap.encoding = A["lb"]), ne(e, s), s.extensions && ae(a, e, s), e
            })
        }, te.prototype.loadGeometries = function (e) {
            var t = this, n = this.extensions, r = this.primitiveCache;

            function a(e) {
                return n[U.KHR_DRACO_MESH_COMPRESSION].decodePrimitive(e, t).then(function (n) {
                    return ie(n, e, t)
                })
            }

            for (var s = [], i = 0, o = e.length; i < o; i++) {
                var l, c = e[i], u = le(c), p = r[u];
                if (p) s.push(p.promise); else l = c.extensions && c.extensions[U.KHR_DRACO_MESH_COMPRESSION] ? a(c) : ie(new A["e"], c, t), r[u] = {
                    primitive: c,
                    promise: l
                }, s.push(l)
            }
            return Promise.all(s)
        }, te.prototype.loadMesh = function (e) {
            for (var t = this, n = this.json, r = n.meshes[e], a = r.primitives, s = [], i = 0, o = a.length; i < o; i++) {
                var l = void 0 === a[i].material ? ue() : this.getDependency("material", a[i].material);
                s.push(l)
            }
            return Promise.all(s).then(function (n) {
                return t.loadGeometries(a).then(function (s) {
                    for (var i = [], o = 0, l = s.length; o < l; o++) {
                        var c, u = s[o], p = a[o], d = n[o];
                        if (p.mode === H.TRIANGLES || p.mode === H.TRIANGLE_STRIP || p.mode === H.TRIANGLE_FAN || void 0 === p.mode) c = !0 === r.isSkinnedMesh ? new A["bb"](u, d) : new A["E"](u, d), !0 !== c.isSkinnedMesh || c.geometry.attributes.skinWeight.normalized || c.normalizeSkinWeights(), p.mode === H.TRIANGLE_STRIP ? c.drawMode = A["fb"] : p.mode === H.TRIANGLE_FAN && (c.drawMode = A["eb"]); else if (p.mode === H.LINES) c = new A["v"](u, d); else if (p.mode === H.LINE_STRIP) c = new A["s"](u, d); else if (p.mode === H.LINE_LOOP) c = new A["u"](u, d); else {
                            if (p.mode !== H.POINTS) throw new Error("THREE.GLTFLoader: Primitive mode unsupported: " + p.mode);
                            c = new A["Q"](u, d)
                        }
                        Object.keys(c.geometry.morphAttributes).length > 0 && pe(c, r), c.name = r.name || "mesh_" + e, s.length > 1 && (c.name += "_" + o), ne(c, r), t.assignFinalMaterial(c), i.push(c)
                    }
                    if (1 === i.length) return i[0];
                    for (var f = new A["m"], m = 0, h = i.length; m < h; m++) f.add(i[m]);
                    return f
                })
            })
        }, te.prototype.loadCamera = function (e) {
            var t, n = this.json.cameras[e], r = n[n.type];
            if (r) return "perspective" === n.type ? t = new A["O"](A["C"].radToDeg(r.yfov), r.aspectRatio || 1, r.znear || 1, r.zfar || 2e6) : "orthographic" === n.type && (t = new A["N"](r.xmag / -2, r.xmag / 2, r.ymag / 2, r.ymag / -2, r.znear, r.zfar)), void 0 !== n.name && (t.name = n.name), ne(t, n), Promise.resolve(t);
            console.warn("THREE.GLTFLoader: Missing camera parameters.")
        }, te.prototype.loadSkin = function (e) {
            var t = this.json.skins[e], n = {joints: t.joints};
            return void 0 === t.inverseBindMatrices ? Promise.resolve(n) : this.getDependency("accessor", t.inverseBindMatrices).then(function (e) {
                return n.inverseBindMatrices = e, n
            })
        }, te.prototype.loadAnimation = function (e) {
            for (var t = this.json, n = t.animations[e], r = [], a = [], s = [], i = [], o = [], l = 0, c = n.channels.length; l < c; l++) {
                var u = n.channels[l], p = n.samplers[u.sampler], d = u.target, f = void 0 !== d.node ? d.node : d.id,
                    m = void 0 !== n.parameters ? n.parameters[p.input] : p.input,
                    h = void 0 !== n.parameters ? n.parameters[p.output] : p.output;
                r.push(this.getDependency("node", f)), a.push(this.getDependency("accessor", m)), s.push(this.getDependency("accessor", h)), i.push(p), o.push(d)
            }
            return Promise.all([Promise.all(r), Promise.all(a), Promise.all(s), Promise.all(i), Promise.all(o)]).then(function (t) {
                for (var r = t[0], a = t[1], s = t[2], i = t[3], o = t[4], l = [], c = 0, u = r.length; c < u; c++) {
                    var p = r[c], d = a[c], f = s[c], m = i[c], h = o[c];
                    if (void 0 !== p) {
                        var v;
                        switch (p.updateMatrix(), p.matrixAutoUpdate = !0, K[h.path]) {
                            case K.weights:
                                v = A["L"];
                                break;
                            case K.rotation:
                                v = A["T"];
                                break;
                            case K.position:
                            case K.scale:
                            default:
                                v = A["ib"];
                                break
                        }
                        var g = p.name ? p.name : p.uuid, T = void 0 !== m.interpolation ? V[m.interpolation] : A["r"],
                            _ = [];
                        K[h.path] === K.weights ? p.traverse(function (e) {
                            !0 === e.isMesh && e.morphTargetInfluences && _.push(e.name ? e.name : e.uuid)
                        }) : _.push(g);
                        var S = f.array;
                        if (f.normalized) {
                            var y;
                            if (S.constructor === Int8Array) y = 1 / 127; else if (S.constructor === Uint8Array) y = 1 / 255; else if (S.constructor === Int16Array) y = 1 / 32767; else {
                                if (S.constructor !== Uint16Array) throw new Error("THREE.GLTFLoader: Unsupported output accessor component type.");
                                y = 1 / 65535
                            }
                            for (var b = new Float32Array(S.length), M = 0, x = S.length; M < x; M++) b[M] = S[M] * y;
                            S = b
                        }
                        for (var E = 0, R = _.length; E < R; E++) {
                            var w = new v(_[E] + "." + K[h.path], d.array, S, T);
                            "CUBICSPLINE" === m.interpolation && (w.createInterpolant = function (e) {
                                return new de(this.times, this.values, this.getValueSize() / 3, e)
                            }, w.createInterpolant.isInterpolantFactoryMethodGLTFCubicSpline = !0), l.push(w)
                        }
                    }
                }
                var L = void 0 !== n.name ? n.name : "animation_" + e;
                return new A["b"](L, void 0, l)
            })
        }, te.prototype.loadNode = function (e) {
            var t = this.json, n = this.extensions, r = this, a = t.meshReferences, s = t.meshUses, i = t.nodes[e];
            return function () {
                var e = [];
                return void 0 !== i.mesh && e.push(r.getDependency("mesh", i.mesh).then(function (e) {
                    var t;
                    if (a[i.mesh] > 1) {
                        var n = s[i.mesh]++;
                        t = e.clone(), t.name += "_instance_" + n, t.onBeforeRender = e.onBeforeRender;
                        for (var r = 0, o = t.children.length; r < o; r++) t.children[r].name += "_instance_" + n, t.children[r].onBeforeRender = e.children[r].onBeforeRender
                    } else t = e;
                    return void 0 !== i.weights && t.traverse(function (e) {
                        if (e.isMesh) for (var t = 0, n = i.weights.length; t < n; t++) e.morphTargetInfluences[t] = i.weights[t]
                    }), t
                })), void 0 !== i.camera && e.push(r.getDependency("camera", i.camera)), i.extensions && i.extensions[U.KHR_LIGHTS_PUNCTUAL] && void 0 !== i.extensions[U.KHR_LIGHTS_PUNCTUAL].light && e.push(r.getDependency("light", i.extensions[U.KHR_LIGHTS_PUNCTUAL].light)), Promise.all(e)
            }().then(function (e) {
                var t;
                if (t = !0 === i.isBone ? new A["c"] : e.length > 1 ? new A["m"] : 1 === e.length ? e[0] : new A["M"], t !== e[0]) for (var r = 0, a = e.length; r < a; r++) t.add(e[r]);
                if (void 0 !== i.name && (t.userData.name = i.name, t.name = A["S"].sanitizeNodeName(i.name)), ne(t, i), i.extensions && ae(n, t, i), void 0 !== i.matrix) {
                    var s = new A["D"];
                    s.fromArray(i.matrix), t.applyMatrix(s)
                } else void 0 !== i.translation && t.position.fromArray(i.translation), void 0 !== i.rotation && t.quaternion.fromArray(i.rotation), void 0 !== i.scale && t.scale.fromArray(i.scale);
                return t
            })
        }, te.prototype.loadScene = function () {
            function e(t, n, r, a) {
                var s = r.nodes[t];
                return a.getDependency("node", t).then(function (e) {
                    return void 0 === s.skin ? e : a.getDependency("skin", s.skin).then(function (e) {
                        t = e;
                        for (var n = [], r = 0, s = t.joints.length; r < s; r++) n.push(a.getDependency("node", t.joints[r]));
                        return Promise.all(n)
                    }).then(function (n) {
                        return e.traverse(function (e) {
                            if (e.isMesh) {
                                for (var r = [], a = [], s = 0, i = n.length; s < i; s++) {
                                    var o = n[s];
                                    if (o) {
                                        r.push(o);
                                        var l = new A["D"];
                                        void 0 !== t.inverseBindMatrices && l.fromArray(t.inverseBindMatrices.array, 16 * s), a.push(l)
                                    } else console.warn('THREE.GLTFLoader: Joint "%s" could not be found.', t.joints[s])
                                }
                                e.bind(new A["ab"](r, a), e.matrixWorld)
                            }
                        }), e
                    });
                    var t
                }).then(function (t) {
                    n.add(t);
                    var i = [];
                    if (s.children) for (var o = s.children, l = 0, c = o.length; l < c; l++) {
                        var u = o[l];
                        i.push(e(u, t, r, a))
                    }
                    return Promise.all(i)
                })
            }

            return function () {
                var t = Object(L["a"])(regeneratorRuntime.mark(function t(n) {
                    var r, a, s, i, o, l, c, u, p;
                    return regeneratorRuntime.wrap(function (t) {
                        while (1) switch (t.prev = t.next) {
                            case 0:
                                for (r = this.json, a = this.extensions, s = this.json.scenes[n], i = this, o = new A["X"], void 0 !== s.name && (o.name = s.name), ne(o, s), s.extensions && ae(a, o, s), l = s.nodes || [], c = [], u = 0, p = l.length; u < p; u++) c.push(e(l[u], o, r, i));
                                return t.next = 13, Promise.all(c);
                            case 13:
                                return t.abrupt("return", o);
                            case 14:
                            case"end":
                                return t.stop()
                        }
                    }, t, this)
                }));

                function n(e) {
                    return t.apply(this, arguments)
                }

                return n
            }()
        }(), de.prototype = Object.create(A["p"].prototype), de.prototype.constructor = de, de.prototype.copySampleValue_ = function (e) {
            for (var t = this.resultBuffer, n = this.sampleValues, r = this.valueSize, a = e * r * 3 + r, s = 0; s !== r; s++) t[s] = n[a + s];
            return t
        }, de.prototype.beforeStart_ = de.prototype.copySampleValue_, de.prototype.afterEnd_ = de.prototype.copySampleValue_, de.prototype.interpolate_ = function (e, t, n, r) {
            for (var a = this.resultBuffer, s = this.sampleValues, i = this.valueSize, o = 2 * i, l = 3 * i, c = r - t, u = (n - t) / c, p = u * u, d = p * u, f = e * l, m = f - l, h = -2 * d + 3 * p, v = d - p, g = 1 - h, T = v - p + u, _ = 0; _ !== i; _++) {
                var S = s[m + _ + i], y = s[m + _ + o] * c, b = s[f + _ + i], M = s[f + _] * c;
                a[_] = g * S + T * y + h * b + v * M
            }
            return a
        };
        var me = {
                components: {Footer: R}, data: function () {
                    return {percent: "100%", isFixed: !0}
                }, mounted: function () {
                    var e = this.$refs.comCanvas, t = new A["X"], n = new z;
                    n.load("/static/model/23-AGWN041-1.gltf", function (e) {
                        console.log("1:obj"), e.scene.children[0].position.set(0, -1, 0), e.scene.name = "root", e.scene.scale.set(2.5, 2.5, 2.5), t.add(e.scene)
                    }, function (e) {
                        console.log(e.loaded / e.total * 100 + "%loaded")
                    }, function (e) {
                        console.log("Error!", e)
                    });
                    var r = new A["a"](5592405);
                    r.intensity = .5, t.add(r), console.log(t);
                    var a = 850, s = 700, i = new A["O"](45, a / s, .1, 1e4);
                    i.position.set(0, 0, 40), i.lookAt(t.position);
                    var o = new A["kb"]({canvas: e, alpha: !0});

                    function l() {
                        o.render(t, i), t.traverse(function (e) {
                            "root" === e.name && (e.rotation.y += .01)
                        }), requestAnimationFrame(l), e.style.width = "100%", e.style.height = "170%"
                    }

                    l.alpha = 0, o.setSize(a, s), o.gammaInput = !0, o.gammaOutput = !0, l()
                }
            }, he = me, ve = (n("6af9"), Object(p["a"])(he, _, S, !1, null, "10a3b693", null)), ge = ve.exports,
            Te = function () {
                var e = this, t = e.$createElement, n = e._self._c || t;
                return n("div", {ref: "main", staticClass: "introduce-wrapper"}, [n("Title", {
                    attrs: {
                        titleImg: e.img,
                        englistTitle: "Product introduction"
                    }
                }), e._l(e.modelList, function (e) {
                    return n("div", {
                        key: e.index,
                        staticClass: "model-list"
                    }, [n("Model", {
                        attrs: {
                            mainTitle: e.mainTitle,
                            explain: e.explain,
                            num: e.index,
                            img: e.img,
                            hover: e.hover,
                            circleColor: e.circleColor
                        }
                    })], 1)
                }), n("Footer", {attrs: {isFixed: e.isFixed}})], 2)
            }, _e = [], Se = function () {
                var e = this, t = e.$createElement, n = e._self._c || t;
                return n("div", {staticClass: "title-wrapper"}, [n("div", {staticClass: "title"}, [n("img", {attrs: {src: e.titleImg}}), n("span", [e._v(e._s(e.englistTitle))])]), e.isPartner ? n("div", {staticClass: "separate"}, [n("div", {staticClass: "separate-top"}), n("div", {staticClass: "separate-bottom"})]) : e._e()])
            }, ye = [], be = {props: {titleImg: String, englistTitle: String, isPartner: Boolean}}, Me = be,
            xe = (n("3d66"), Object(p["a"])(Me, Se, ye, !1, null, "718f4f25", null)), Ee = xe.exports,
            Re = function () {
                var e = this, t = e.$createElement, n = e._self._c || t;
                return n("div", {
                    staticClass: "model-wrapper",
                    style: {background: e.bgColor},
                    on: {mouseenter: e.enter, mouseleave: e.leave}
                }, [n("div", {staticClass: "model"}, [n("h3", [n("span", {staticClass: "round"}), e._v(e._s(e.mainTitle))]), n("p", [e._v(e._s(e.explain))])]), n("div", {staticClass: "shoes-box"}, [n("div", {staticClass: "shoes-inner"}, [n("img", {
                    attrs: {
                        src: "img",
                        alt: e.mainTitle
                    }
                })])]), n("div", {staticClass: "num-box"}, [n("div", {
                    staticClass: "num-round",
                    style: {borderColor: e.circle}
                }), n("span", [e._v(e._s(e.num))])])])
            }, Ae = [], we = {
                props: {
                    mainTitle: String,
                    explain: String,
                    img: String,
                    num: String,
                    circleColor: String,
                    hover: String
                }, data: function () {
                    return {bgColor: "", circle: ""}
                }, methods: {
                    enter: function () {
                        this.bgColor = this.hover, this.circle = this.circleColor
                    }, leave: function () {
                        this.bgColor = "", this.circle = ""
                    }
                }
            }, Le = we, Ce = (n("21da"), Object(p["a"])(Le, Re, Ae, !1, null, "20250c5c", null)), Fe = Ce.exports, Ie = {
                components: {Title: Ee, Model: Fe, Footer: R}, data: function () {
                    return {
                        isFixed: !1,
                        img: n("e3c9"),
                        modelList: [{
                            mainTitle: "3D模型",
                            explain: "作为全球领先的移动增强现实交互公司，“足购科技”拉近传统鞋业 与数字媒体之间的距离。使用“足购”的增强现实交互功能，消费者可以通过他们的智能手机",
                            index: "01",
                            img: "",
                            hover: "#09D293",
                            circleColor: "#1A09D5"
                        }, {
                            mainTitle: "AR展陈",
                            explain: "作为全球领先的移动增强现实交互公司，“足购科技”拉近传统鞋业 与数字媒体之间的距离。使用“足购”的增强现实交互功能，消费者可以通过他们的智能手机",
                            index: "02",
                            img: "",
                            hover: "#0DC7D8",
                            circleColor: "#2AFFEA"
                        }, {
                            mainTitle: "AR试穿",
                            explain: "作为全球领先的移动增强现实交互公司，“足购科技”拉近传统鞋业 与数字媒体之间的距离。使用“足购”的增强现实交互功能，消费者可以通过他们的智能手机",
                            index: "03",
                            img: "",
                            hover: "#1866DB",
                            circleColor: "#43FFC4"
                        }]
                    }
                }, mounted: function () {
                    var e = document.documentElement.clientHeight || document.body.clientHeight,
                        t = this.$refs.main.offsetHeight;
                    this.isFixed = !(t > e)
                }
            }, Oe = Ie, Pe = (n("0ecc"), Object(p["a"])(Oe, Te, _e, !1, null, "695ec300", null)), Ne = Pe.exports,
            Ue = function () {
                var e = this, t = e.$createElement, r = e._self._c || t;
                return r("div", {
                    ref: "main",
                    staticClass: "partner-wrapper"
                }, [r("div", {staticClass: "partner-title"}, [r("Title", {
                    attrs: {
                        titleImg: e.img,
                        englistTitle: "Cooperative partner",
                        isPartner: ""
                    }
                })], 1), r("div", {staticClass: "content"}, [r("div", {staticClass: "left-box"}), r("div", {
                    ref: "box",
                    staticClass: "scroll"
                }, [r("img", {
                    ref: "img",
                    attrs: {src: n("08cb")}
                }), r("img", {attrs: {src: n("08cb")}})]), r("div", {staticClass: "right-box"})]), r("Footer", {attrs: {isFixed: e.isFixed}})], 1)
            }, He = [], De = {
                components: {Title: Ee, Footer: R}, data: function () {
                    return {isFixed: !1, img: n("f2ab")}
                }, mounted: function () {
                    this.toScroll(), this.onFixed()
                }, methods: {
                    toScroll: function () {
                        var e = this.$refs.box, t = this.$refs.img, n = 0;
                        e.style = "width: ".concat(2 * t.offsetWidth, "px "), setInterval(function () {
                            n++, n >= t.offsetWidth && (n = 0), e.style = "transform: translateX(-" + n + "px)"
                        }, 10)
                    }, onFixed: function () {
                        var e = document.documentElement.clientHeight || document.body.clientHeight,
                            t = this.$refs.main.offsetHeight;
                        this.isFixed = !(t > e)
                    }
                }
            }, Ge = De, ke = (n("4066"), Object(p["a"])(Ge, Ue, He, !1, null, "cddf83f4", null)), je = ke.exports,
            Be = function () {
                var e = this, t = e.$createElement, n = e._self._c || t;
                return n("div", {staticClass: "about-wrapper"}, [n("Title", {
                    attrs: {
                        titleImg: e.img,
                        englistTitle: "About zugo"
                    }
                }), e._m(0), n("Footer", {attrs: {isFixed: e.isFixed}})], 1)
            }, Ke = [function () {
                var e = this, t = e.$createElement, r = e._self._c || t;
                return r("div", {staticClass: "content"}, [r("div", {staticClass: "zg-logo"}, [r("img", {attrs: {src: n("8c45")}})]), r("div", {staticClass: "zg-container"}, [r("h2", [e._v("About zugo")]), r("h3", [e._v("关于足购")]), r("p", [e._v("作为全球领先的移动增强现实交互公司，“足购科技”拉近传统鞋业与数字媒体之间的距离。")]), r("p", [e._v("使用“足购”的增强现实交互功能，消费者可以通过他们的智能手机或平板电脑获得神奇的交互体验。这是革命性的营销方式！")])])])
            }], Ve = {
                components: {Title: Ee, Footer: R}, data: function () {
                    return {isFixed: !1, img: n("66bc")}
                }, mounted: function () {
                    var e = document.documentElement.clientHeight || document.body.clientHeight,
                        t = this.$refs.main.offsetHeight;
                    this.isFixed = !(t > e)
                }
            }, Xe = Ve, $e = (n("d17e"), Object(p["a"])(Xe, Be, Ke, !1, null, "581017ef", null)), ze = $e.exports,
            Ye = function () {
                var e = this, t = e.$createElement, n = e._self._c || t;
                return n("div", {staticClass: "contact-wrapper"}, [n("div", {staticClass: "banner"}), e._m(0), n("Footer", {attrs: {isFixed: e.isFixed}})], 1)
            }, We = [function () {
                var e = this, t = e.$createElement, r = e._self._c || t;
                return r("div", {staticClass: "contact"}, [r("div", {staticClass: "title"}, [r("img", {attrs: {src: n("e82c")}}), r("p", [e._v("Contact us")])]), r("div", {staticClass: "container"}, [r("p", [e._v("电话：0571-88581570")]), r("p", [e._v("联系人：李先生")]), r("p", [e._v("手机：138-5772-5101")]), r("p", [e._v("邮件：liwangyang@zugo.vip")]), r("p", [e._v("地址：杭州市余杭区仓恒生科技园16号楼2单元5楼")])])])
            }], Ze = {
                components: {Footer: R}, data: function () {
                    return {isFixed: !1}
                }, mounted: function () {
                    var e = document.documentElement.clientHeight || document.body.clientHeight,
                        t = this.$refs.main.offsetHeight;
                    this.isFixed = !(t > e)
                }
            }, Je = Ze, qe = (n("e819"), Object(p["a"])(Je, Ye, We, !1, null, "708d2d7f", null)), Qe = qe.exports;
        a["a"].use(T["a"]);
        var et = new T["a"]({
            routes: [{path: "/", redirect: "/home"}, {
                path: "/home",
                component: ge
            }, {path: "/introduce", component: Ne}, {path: "/partner", component: je}, {
                path: "/about",
                component: ze
            }, {path: "/contact", component: Qe}]
        }), tt = n("2f62");
        a["a"].use(tt["a"]);
        var nt = new tt["a"].Store({state: {}, mutations: {}, actions: {}});
        n("9536");
        a["a"].config.productionTip = !1, new a["a"]({
            router: et, store: nt, render: function (e) {
                return e(g)
            }
        }).$mount("#app")
    }, "61f8": function (e, t, n) {
        e.exports = n.p + "img/art-title.12d470b9.png"
    }, "66bc": function (e, t, n) {
        e.exports = n.p + "img/about-title.b9a14dc6.png"
    }, "6af9": function (e, t, n) {
        "use strict";
        var r = n("ec25"), a = n.n(r);
        a.a
    }, "6cb6": function (e, t, n) {
        e.exports = n.p + "img/sub-title.a192cfcb.png"
    }, "8c45": function (e, t, n) {
        e.exports = n.p + "img/about-logo.293d33ad.png"
    }, 9007: function (e, t, n) {
    }, 9536: function (e, t, n) {
    }, "9a2a": function (e, t, n) {
    }, "9e5a": function (e, t, n) {
    }, ac75: function (e, t, n) {
        "use strict";
        var r = n("9a2a"), a = n.n(r);
        a.a
    }, d17e: function (e, t, n) {
        "use strict";
        var r = n("18f8"), a = n.n(r);
        a.a
    }, dd02: function (e, t, n) {
        "use strict";
        var r = n("9007"), a = n.n(r);
        a.a
    }, de19: function (e, t, n) {
    }, e3c9: function (e, t, n) {
        e.exports = n.p + "img/introduce-title.138cb1e4.png"
    }, e819: function (e, t, n) {
        "use strict";
        var r = n("de19"), a = n.n(r);
        a.a
    }, e82c: function (e, t, n) {
        e.exports = n.p + "img/contact-title.acaf5cf6.png"
    }, e8f0: function (e, t, n) {
    }, ec25: function (e, t, n) {
    }, f2ab: function (e, t, n) {
        e.exports = n.p + "img/partner-title.9f2c9500.png"
    }
});
//# sourceMappingURL=app.717be82b.js.map